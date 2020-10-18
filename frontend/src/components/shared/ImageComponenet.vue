<template>
  <div>
    <v-card flat>
        <v-img :src="image_src" :height="height" :width="width"></v-img>
    <v-card-subtitle>
        {{caption}}
    </v-card-subtitle>
    </v-card>
  </div>
</template>

<script>
export default {
    props:{
        caption: String,
        image_src: String,
        height: String,
        width: String
    }
}
</script>