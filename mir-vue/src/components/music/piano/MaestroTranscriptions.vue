<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />

      </v-flex>
      <v-flex md10>
        <v-card flat>

          <v-card-title>
            Maestro Transcription Training Examples Results
          </v-card-title>

        <v-data-table
          v-model="selected"  
          :headers="headers"
          :items="getMaestroTraningData" >

        <template v-slot:item="{ item }">
            <tr @click="rowClicked(item.fileID)">
                <td>{{item.title}}</td>
                <td>{{item.composer}}</td>
            </tr>

        </template>
      </v-data-table>

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>


</template>

<script>

import { mapGetters, mapActions } from "vuex";
import router from '../../../router'
import BaseNavBar from  '../../BaseNavBar'
export default {
    components:{
      BaseNavBar
    },
    created(){
      this.fetchMaestroTrainingData()
      
    //   axios.get("http://localhost:8081/maestro").then((response) => {

    //     var response_string = JSON.stringify(response.data)
    //     var data = JSON.parse(response_string)
    //     this.data = data

    //   }, (error) => {
    //     console.log(error);
    //   });
    },

    mounted() {
    },
    
    computed:{
      ...mapGetters(["getMaestroTraningData"])
    },

    methods:{
      ...mapActions(["fetchMaestroTrainingData"]),     
      rowClicked(fileID){
        router.push({ name: 'piano-transcription', params: { fileID: fileID } })
      },
      ...mapActions(["fetchTrainingData"]),    

  },
  props:{

  },
  data(){
    return {
      items: [
        { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
        { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
        { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
        { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
        { title: 'Transcriptions', icon: 'mdi-help-box', route:'/transcriptions' },

      ],
      selected:[],
      trainingData: [],

      page: 1,
      
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