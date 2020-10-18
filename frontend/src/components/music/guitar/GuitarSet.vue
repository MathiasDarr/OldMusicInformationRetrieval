<template>
  <v-container>
  
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
    <v-flex md10>

      <v-card flat height="300px">
        <v-container>
          <v-layout>
            <v-flex md12>
              <v-card flat>
                <v-card-title> Music Information Retrieval </v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  Below is a table of all training examples from guitarset.  Click on a row to view generated tablature & listen to audio served by Cloudfront.
                </v-card-text>
                
              </v-card>
            </v-flex>

          </v-layout>
        </v-container>


        
        <v-data-table
          v-model="selected"  
          :headers="headers"
          :items="getGuitarsetData" > 

        <template v-slot:item="{ item }">
            <tr @click="rowClicked(item.fileID, item.title)">
                <td>{{item.title}}</td>
            </tr>
        </template>
        </v-data-table>
      </v-card>
 
    <router-view></router-view>
    
    </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

import { mapGetters, mapActions } from "vuex";
import router from '../../../router'
import BaseNavBar from  '../../BaseNavBar'



export default {
    created(){
      this.fetchGuitarsetData()
    },
    
    components:{
      BaseNavBar
    },

    mounted() {

    },
    
    computed:{
      ...mapGetters(["getGuitarsetData"])
    },

    methods:{
      // ...mapActions(["getS3Transcription"]),     
      rowClicked(fileID, title){
        console.log("clicked on title " + title)
        router.push({ name: 'transcription_detail', params: { fileID: fileID, title: title} })
      },
      ...mapActions(["fetchGuitarsetData"]),    

    },
    props:{

    },

    data(){
        return {
        selected:[],
        trainingData: [],

        page: 1,
        

        items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              // { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
          ],

        headers: [
            {
            text: 'Training Example',
            align: 'start',
            sortable: false,
            value: 'title',
            },


        ],
    }
  }


  
}
</script>