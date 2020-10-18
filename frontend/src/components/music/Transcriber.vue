<template>
  <v-container>
    <v-layout>
      <v-flex md2>
          <BaseNavBar v-bind:items=items />
      </v-flex>

      <v-flex  md10>

        <v-container>
          <v-layout>
            <v-flex md8>
              <h3> Transcriber Service </h3>
            </v-flex>
            <v-flex md4>
              <v-btn color="primary" @click="login()">Login </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
        

        <v-card flat> 
          <v-card-text>
            <div v-if="email != false">
              
              Welcome {{email}} 


              <TranscriptionList v-bind:email = email />


            </div>
            <div v-else>
              Sign in to view and create transcriptions 
            </div>

            <PostTranscription />
          </v-card-text>
        </v-card>


        <!-- <v-card flat>
          
          <v-card-title>
          Transcription Service
          </v-card-title>

          <UploadFile />

        </v-card> -->
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

import BaseNavBar from  '../BaseNavBar'
import UploadFile from '../uploads/UploadFile'
import { mapGetters, mapActions } from "vuex";
import router from '../../router'
import TranscriptionList from './TranscriptionList'
import PostTranscription from './PostTranscription'


export default {
  methods:{
    ...mapActions(["fetchUsersTranscriptions", "postTranscription"]),
    login(){
      router.push({ name: 'register'})
    },
    post(){
      var transcription = {title:this.title, content: this.content, userID:this.getEmail}
     
      // var transcription = {title:"Bugaboo in C minor", content: "This song blows!", userID:"mddarr@gmail.com"}
      this.postTranscription(transcription)
    },
  },


  created(){
    console.log("The email ooutside the if is " + this.getEmail)
    if(this.getEmail != false){
      console.log("The email is " + this.getEmail)
          var email = this.getEmail
          var parsed_email = email.split('@')[0]
          console.log(parsed_email)
          this.email=parsed_email
          this.fetchUsersTranscriptions(email)
    }else{
      this.email = false
    }
  },
  computed:{
    ...mapGetters(["getEmail", "getUsersTranscriptions"]),
  },


  components:{
    BaseNavBar,
    UploadFile,
    TranscriptionList,
    PostTranscription
  },
  data(){

        return {
            title: '',
            content: '',
            types: ['guitar', 'piano'],
            items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },

          ],

        }
    }
}
</script>