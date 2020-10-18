<template>
    <v-layout>
        <v-flex md1>
            <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/github.png'" height="60px" width="60"></v-img>
        </v-flex>
        <v-flex md8>
          <div class="title font-weight-medium">
            Github Link: 
            <a :href='link'>{{ link_title}}</a> 
          </div>

        </v-flex>
    </v-layout>
</template>


<script>
export default {


      props:{
        links: Array,
        link_titles: Array,
        link: String,
        link_title:String
    }
}
</script>