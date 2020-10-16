<template>
  <v-container>
    <v-layout>
        <v-flex md2>
          <BaseNavBar v-bind:items=items />
        </v-flex>
        <v-flex  md4>

          <v-card flat>
            <v-list two-line>
            <v-list-item-group >
                <template v-for="(item, index) in getUsersTranscriptions">
                  <v-list-item :key="item.title">
                
                    <template>
                    
                      <v-list-item-content @click="selectTranscription(item.id)">
                        <v-list-item-title v-text="item.title"></v-list-item-title>
                        <v-list-item-subtitle class="text--primary">Guitar </v-list-item-subtitle>
                      </v-list-item-content>

                    </template>
                  </v-list-item>

                  <v-divider
                    v-if="index + 1 < items.length"
                    :key="index">
                  </v-divider>
                
                </template>
              </v-list-item-group>
            </v-list>  
          </v-card>



          <!-- <v-card flat class="pa-3" v-for="transcription in getUsersTranscriptions" :key="transcription.id" >
            <v-container dark>
              <v-layout row>
                <v-flex xs7 sm8 md9>
                  <v-card-title>
                    <div>
                      <v-flex >
                        <p class="font-weight-light grey--text"> {{transcription.title}}</p>
                      </v-flex>
                      <div> 
                          
                        <v-btn text small v-on:click="selectTranscription(transcription.id)" > View Transcription </v-btn>
                      </div>
                    </div>
                  </v-card-title>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>  -->
        </v-flex>



        
    </v-layout>
  </v-container>
</template>


<script>
/* eslint-disable */
import { mapGetters, mapActions } from "vuex";
import router from '../../router'
import BaseNavBar from  '../BaseNavBar'


export default {
    components:{
        BaseNavBar
    },
    data(){
        return {
            email:"mddarr@gmail.com",
            items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
              { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
              { title: 'Transcriptions', icon: 'mdi-help-box', route:'/transcriptions_list' },
            ],
        }
    },
    created(){
        console.log("WHAT LEREFDF ")
        this.fetchUsersTranscriptions(this.email)
    },


    methods:{
        ...mapActions(["fetchUsersTranscriptions"]),
        selectTranscription(id){
            router.push('/transcription')
        },
    },

    // props:{
    //     email: String
    // },
    computed:{
    ...mapGetters(["getUsersTranscriptions"]),
    }
}
</script>