<template>
  <div>
    <v-container>
        <v-layout row>
      <v-flex md6>
        <v-card flat >
          <v-layout row>
            <v-flex xs112 sm6 offset-sm1>
              <v-btn raised class="primary" @click="onPickFile"> Upload {{ button_title }} Image </v-btn>
              <input type ="file" style ="display: none" ref="fileInput" accept="image/*" @change="onFilePicked">
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>

            </v-flex>
            
          </v-layout>
            
        </v-card>
      </v-flex>
    
        <v-flex md6>
          <v-card flat>
            <div v-if="imageUrl == '-1'">
            </div>
            <div v-else>
                <img :src="imageUrl" height ="360" width="500">
            </div>
            
          </v-card>
        </v-flex>
        </v-layout>
    </v-container>
  </div>
</template>


<script>

import { mapGetters, mapActions } from "vuex";

export default {
   data(){
       return {
           imageUrl:-1,
       }
   },
   props:{
     button_title:String
   },
   created(){
        if(this.baseImageSelection != -2 && this.button_title =='Base'){
          this.readImageFile(this.baseImageSelection)
          console.log("hey hey what can i do")
        }else if(this.styleImageSelection != -2 && this.button_title == 'Style'){
          this.readImageFile(this.styleImageSelection)
        }
        else if(this.styleImageSelection != -2 && this.button_title == 'Style'){
          this.readImageFile(this.styleImageSelection)
        }
        else if(this.getReportThumbail != -2 && this.button_title == 'Report'){
          this.readImageFile(this.styleImageSelection)
        }


        const fileReader = new FileReader();
          fileReader.addEventListener('load',() => {
          this.imageUrl = fileReader.result
        })
   },
    methods:{
        ...mapActions(["setBaseImageSelection"]),
        ...mapActions(["setStyleImageSelection"]),
        ...mapActions(["setReportThumbnail"]),
        onCreateReport(){
          if(!this.formIsValid){
            return
          }
        },
        
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        onFilePicked(event){
          const files = event.target.files
          let filename = files[0].name;

          if (filename.lastIndexOf('.') <= 0){
            return alert('please add a valid file')
          }

          this.readImageFile(files[0])
        },

        readImageFile(file){
          const fileReader = new FileReader();
          fileReader.addEventListener('load',() => {
            this.imageUrl = fileReader.result
          })
          fileReader.readAsDataURL(file)
          if(this.button_title == 'Style'){
                this.setStyleImageSelection(file)
          }else if(this.button_title=='Base'){
                this.setBaseImageSelection(file)
          }
          else if(this.button_title=='Report'){
                this.setReportThumbnail(file)
          }
          
        },

        onPickFile(){
          this.$refs.fileInput.click()
        },
     },
     computed:{
        ...mapGetters(["styleImageSelection"]),
        ...mapGetters(["baseImageSelection"]),
        ...mapGetters(['getReportThumbail'])

     }
   

}
</script>