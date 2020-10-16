import boto3
import os
import logging
import time
import librosa
from numpy import format_float_positional
import boto3
import json
import numpy as np


class Transcription:
    def __init__(self, wav, notes, user, title):
        self.user = user
        self.title = title
        self.transcription_path = '{}/{}.json'.format(user, title)
        try:
            os.mkdir(user)
        except Exception as e:
            print(e)

        self.bucket = 'dakobed-transcriptions'
        y, sr = librosa.load(wav)
        tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
        self.beats = [float(format_float_positional(beat, 3)) for beat in beat_times]
        self.assign_notes_to_measures(notes)
        self.processMeasures()
        self.generate_transcription_json()
        os.rmdir(user)

    def get_transcription_path(self):
        return self.transcription_path

    def getUser(self):
        return self.getUser()

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

    def getBucket(self):
        return self.getBucket()

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

        with open(self.transcription_path, 'w') as outfile:
            json.dump(transcription, outfile)

        bucket = 'dakobed-guitarset'
        s3 = boto3.client('s3')
        with open(self.transcription_path, "rb") as f:
            s3.upload_fileobj(f, bucket, self.transcription_path)

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


def perform_transform(messagebody):
    user = messagebody['user']
    wavpath = messagebody['path']
    bucket = messagebody['bucket']

    with open('audio.wav', 'wb') as f:
        s3.download_fileobj(bucket, wavpath, f)
    y, sr = librosa.load('audio.wav')
    cqt = librosa.amplitude_to_db(np.abs(librosa.core.cqt(y, sr=sr, n_bins=144, bins_per_octave=24, fmin=librosa.note_to_hz('C2'), norm=1))).T
    np.save('cqt.npy', cqt)
    s3_cqt_path = wavpath.split('/')[1].split('.')[0] + '.npy'
    print("s3 audio path " + str(s3_cqt_path))
    with open('cqt.npy', "rb") as f:
        s3.upload_fileobj(f, bucket, '{}/{}'.format(user, s3_cqt_path))
    os.remove('cqt.npy')
    os.remove('audio.wav')
    return bucket, user, s3_cqt_path, wavpath

def parse_transcription(messagebody):
    wavpath = messagebody['wavpath']
    notespath = messagebody['notespath']
    bucket = messagebody['bucket']
    title = messagebody['title']
    user = messagebody['user']
    s3 = boto3.client('s3')
    with open(wavpath, 'wb') as f:
        s3.download_fileobj(bucket, wavpath, f)
    with open(notespath, 'wb') as f:
        s3.download_fileobj(bucket, wavpath, f)
    with open(notespath, 'r') as f:
        notes = json.load(f)

    transcription = Transcription(wavpath, notes, user, title)
    transcription_path = transcription.get_transcription_path()
    bucket = transcription.getBucket()
    return bucket, transcription_path, user


LOG_FILENAME = '/var/log/ulog.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

sqs = boto3.resource('sqs', region_name='us-west-2')
s3 = boto3.client('s3')

dakobed_transform_queue = sqs.get_queue_by_name(QueueName='DakobedTransformQueue')
dakobed_transcription_queue = sqs.get_queue_by_name(QueueName="DakobedTranscriptionQueue")
dakobed_stop_ec2_queue = sqs.get_queue_by_name(QueueName = "DakobedEC2StopQueue")

while True:
    for message in dakobed_transform_queue.receive_messages():
        try:
            messagebody = message.body
            messagebody = json.loads(messagebody)
            


            # if messagebody['type'] =='transforms':
            #     bucket, user, s3_cqt_path, wavpath = perform_transform(messagebody)
            #     dakobed_transcription_queue.send_message(MessageBody=json.dumps({'bucket': bucket, 'user': user, 'wavpath': wavpath,'path': '{}/{}'.format(user, s3_cqt_path)}))
            # if messagebody['type'] == 'transscription':
            #     bucket, transcription_path, user = parse_transcription(messagebody)
            #     dakobed_stop_ec2_queue.send_message({'bucket': bucket, 'transcription_path': transcription_path, 'user':user})
            message.delete()
        except Exception as e:
            logging.info(e)
            print(e)


    time.sleep(100)