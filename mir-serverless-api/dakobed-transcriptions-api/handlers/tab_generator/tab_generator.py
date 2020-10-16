from numpy import format_float_positional


class Transcription:
    def __init__(self, wav, jam, fileID):
        notes = jam_to_notes_matrix(jam)
        self.fileID = fileID
        y, sr = librosa.load(wav)
        tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
        self.beats = [float(format_float_positional(beat, 3)) for beat in beat_times]
        self.assign_notes_to_measures(notes)
        self.processMeasures()
        self.generate_transcription_json()

    def processMeasures(self):
        measures = []
        for i, notes in enumerate(self.measures_notes):
            try:
                measures.append(Measure(notes, i))
            except Exception as e:
                print(e)
        self.measures = measures

    def getMeasures(self):
        return self.measures

    def assign_notes_to_measures(self, notes):
        measures_end_times = self.beats[0::4]
        nmeasures = len(self.beats) // 4
        if len(self.beats) % 4 != 0:
            nmeasures += 1
        measures = [[] for i in range(nmeasures)]
        measure_index = 0
        current_measure_end = measures_end_times[measure_index]

        for note in notes:
            note[0] = format_float_positional(note[0], 2)

        for note in notes:
            if note[0] > current_measure_end:
                measure_index += 1
                if measure_index >= len(measures):
                    break
                measures[measure_index].append((note))
                current_measure_end = measures_end_times[measure_index]
            else:
                measures[measure_index].append(list(note))
        self.measures_notes = measures

    def generate_transcription_json(self):
        transcription = []
        for m, measure in enumerate(self.measures):
            notes = measure.notes
            beats = measure.note_beats
            durations = measure.note_durations
            for i in range(len(notes)):
                note_dictionary = {'measure':str(m),'midi': str(notes[i][2]), 'string': str(notes[i][3]), 'beat':str(beats[i])}
                transcription.append(note_dictionary)
        with open('data/dakobed-guitarset/fileID{}/transcription.json'.format(self.fileID), 'w') as outfile:
            json.dump(transcription, outfile)
        bucket = 'dakobed-guitarset'
        s3 = boto3.client('s3')
        with open('data/dakobed-guitarset/fileID{}/transcription.json'.format(self.fileID), "rb") as f:
            s3.upload_fileobj(f, bucket, 'fileID{}/transcription.json'.format(self.fileID, self.fileID))


class Measure:
    def __init__(self, notes, index):
        start_of_measure = notes[0][0]
        end_of_measure = notes[-1][0]
        measureduration = notes[-1][0] -notes[0][0]
        sixteenth_note_duration = measureduration/16
        sixteenth_note_buckets = np.linspace(start_of_measure, end_of_measure, 16)

        # This will only be relevant when I am processing piano transcriptions.  An array containing the
        # durations of 1/16, 1/8th, 1/4, quarter dot, 1/2, 1/2 dot & whote notes for this measure.  I w

        note_durations = np.array([sixteenth_note_duration, sixteenth_note_duration*2, sixteenth_note_duration*4,
                                   sixteenth_note_duration*6, sixteenth_note_duration * 8, sixteenth_note_duration * 12,
                                   sixteenth_note_duration*16])

        processed_note_beats = []
        processed_note_durations = []

        for note in notes:
            absolute_val_beat_times_array = np.abs(sixteenth_note_buckets - note[0])
            note_beat = absolute_val_beat_times_array.argmin()
            processed_note_beats.append(note_beat)

            absolute_val_note_durations_array = np.abs(note_durations - note[1])
            duration = absolute_val_note_durations_array.argmin()
            processed_note_durations.append(duration)

        self.note_durations = processed_note_durations
        self.note_beats = processed_note_beats
        self.notes = notes
