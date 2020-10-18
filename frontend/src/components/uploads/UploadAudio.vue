<template>
  <div>
    <v-container>
      <v-layout row>
        <v-flex md6>
          <v-card flat >
            <v-layout row>
              <v-flex xs112 sm6 offset-sm1>
                <v-btn raised class="primary" @click="onPickFile"> Upload Audio </v-btn>
                <input type ="file" style ="display: none" ref="fileInput" accept="audio/*" @change="onFilePicked">
              </v-flex>
            </v-layout>

            
          </v-card>
        </v-flex>
    
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
    methods:{
        ...mapActions(["setUploadedAudioFile"]),

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
          
        },

        onPickFile(){
            this.$refs.fileInput.click()
        },
    },
    
}
</script>