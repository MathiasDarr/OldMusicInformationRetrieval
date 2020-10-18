<template>
  <div>
    <h3>{{title}}</h3>
    <p class="title font-weight-light">
      {{ text }}
    </p>   
  </div>
</template>


<script>
export default {
    props:{
        title:String,
        text:String
    }
}
</script>