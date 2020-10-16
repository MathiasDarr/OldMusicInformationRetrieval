<template>
  <v-container>
    <v-layout>
      <!-- <v-flex md2>
          <BaseNavBar v-bind:items=items />
      </v-flex> -->
      <v-flex md10>
          <v-card tile flat>

            <v-container>
              <v-layout row>
                  <v-flex md 4>
                      <v-form class ="px-3">
                        <v-text-field label ="Title" v-model="title"></v-text-field>
                        <v-btn color="primary" @click="post()">Post</v-btn>
                      </v-form>
                  </v-flex>
                  <v-flex md4 offset-2>
                    <v-radio-group v-model="radioGroup">
                        <v-radio
                            v-for="selection in types" :key="selection.id"
                            :label="selection.type">
                        </v-radio>
                    </v-radio-group>
                  </v-flex>
              </v-layout>
            </v-container>


<!-- 
            <v-form class ="px-3">
                <v-text-field label ="Title" v-model="title"></v-text-field>

                <v-flex>
                    <v-btn @click="post()">Post</v-btn>
                </v-flex>
            </v-form> -->


          </v-card>





      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>

import { mapActions } from "vuex";

export default {
    components:{

    },
    methods:{
        ...mapActions(["postTranscription"]),
        post(){

            var transcription = {title:this.title, type: this.types[this.radioGroup].type, userID:this.email}
            this.postTranscription(transcription)
        }
    },
    data(){
        return {
            types: [{id:0, type: 'Guitar'},{id:1, type:'Piano'}],
            title: '',
            radioGroup:0,
            email: "mddarr@gmail.com",
            items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
              { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
              { title: 'Transcriptions', icon: 'mdi-help-box', route:'/transcriptions_list' },
            ],
        }
    },
}
</script>