<template>
    <div class="text-center">
      
      <v-card>
        <v-card-title>
            GuitarSet Transcription Training Examples
         </v-card-title>
      </v-card>

    <v-data-table
        v-model="selected"  
        :headers="headers"
        :items="getGuitarsetData"
      > 
      <template v-slot:item="{ item }">
            <tr @click="rowClicked(item.fileID)">
                <td>{{item.title}}</td>
            </tr>
        </template>
      </v-data-table>

      <router-view></router-view>
    </div>
</template>

<script>

import { mapGetters, mapActions } from "vuex";

import router from '../../../router'

export default {
    
    created(){
      this.fetchGuitarsetData()
      // const api_gateway_url = 'http://dakobed-nlb-8da0b69cbdc6185f.elb.us-west-2.amazonaws.com/guitarset'
      // axios.get(api_gateway_url).then((response) => {

      //   var response_string = JSON.stringify(response.data)
      //   var data = JSON.parse(response_string)
      //   this.data = data

      // }, (error) => {
      //   console.log(error);
      // });
    },

    components:{

    },
    mounted() {

    },
    
    computed:{
      ...mapGetters(["getGuitarsetData"])
    },

    methods:{
      // ...mapActions(["getS3Transcription"]),     
      rowClicked(fileID){
        router.push({ name: 'transcription_detail', params: { fileID: fileID } })
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