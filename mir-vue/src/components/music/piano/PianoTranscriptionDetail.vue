<template>
  <div>
      Transcription Detail {{fileID}}

    <!-- <audio id="audio" controls>
      <source  id="audioSource" src="" type="audio/wav">
    </audio> -->
          <v-card flat class="pa-3" v-for="line in getLines.slice(0,1)" :key="line.id" >
            <PianoLine  v-bind:notes="line.notes"/>
          </v-card>

  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import PianoLine from './PianoLine'





export default {
  created(){
    this.fileID = this.$route.params.fileID
    this.fetchMaestroTranscription()
  },
  
  methods:{
    ...mapActions(["fetchMaestroTranscription"]),
  },


  props:{
      // fileID:Number
  },

  data(){
    return {
        audioURL:"http://d3rak0tzwsp682.cloudfront.net/fileID3/3audio.wav",
        transcriptionurl:"http://d3rak0tzwsp682.cloudfront.net/fileID" + this.fileID + "/" + this.fileID + "transcription.json"
    }
  },
  computed: {
    ...mapGetters(["getNotes"]),
    ...mapGetters(["getLines"])

  },
  components:{

    PianoLine
  },
  mounted(){

    // var audio = document.getElementById('audio');

    // var source = document.getElementById('audioSource');
    // source.src = "http://d3rak0tzwsp682.cloudfront.net/fileID" + this.fileID + "/" + this.fileID + "audio.wav"

    // audio.load(); //call this to just preload the audio without playing
    // audio.play(); //call this to play the song right away
  }
  
}
</script>

