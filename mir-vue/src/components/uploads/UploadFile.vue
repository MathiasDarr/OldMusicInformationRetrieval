<template>
  <div class="upload">


    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <!-- <v-btn
            class="primary"
            :disabled="!formIsValid"
            type="submit">Upload Audio File</v-btn> -->
          </v-flex>
      </v-layout>

      Select a file
      <input type="file" @change="onFileSelected">
      <div class="my-2">
        <v-btn dark color="primary" @click="onUpload">Upload Audio File</v-btn>
      </div>
      <!-- <button @click="onUpload">Upload </button> -->
  </div>
</template>

<script>
/* eslint-disable */

import axios from 'axios'
import { mapActions } from "vuex";
export default {
    name: 'UploadComponent',
    props: {
        msg: String
    },
    data(){
        return{
            selectedFile:null
        }
    },
    methods:{
        ...mapActions(["uploadFile"]),    

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
          const fileReader = new FileReader();
          fileReader.addEventListener('load')
          fileReader.readAsDataURL(files[0])

        },

        onPickFile(){
          this.$refs.fileInput.click()
        },
        onUpload(){
          const fd = new FormData()
          fd.append('file', this.selectedFile, this.selectedFile.name, fd)

          this.uploadFile()

          // var authOptions = {
          //   method:'POST',
          //   url:'https://vzmta1umza.execute-api.us-west-2.amazonaws.com/v1/upload',
          //   data:{
          //     file:
          //   }
          // }

          // var obj = JSON.stringify(fd);
          // console.log("The form data looks like " + obj)
          // fd.append('file', this.selectedFile, this.selectedFile.name, fd)
          // var obj = JSON.stringify(fd);
          // console.log("The form data looks like " + obj)
          // axios.post(api_url,fd).then(res => {
          //     console.log(res)
          //   });
        }
    },computed:{
      formIsValid () {
        return this.title !== '' &&
          this.location !== '' &&
          this.imageUrl !== '' &&
          this.description !== ''
      },
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
