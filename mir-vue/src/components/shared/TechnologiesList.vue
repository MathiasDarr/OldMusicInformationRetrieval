<template>
  <div>
    <h3> Technologies Used </h3>
    <ul class="title font-weight-light">
      <li v-for="item in technologies" :key="item.message">
        {{ item}}
      </li>
    </ul>
  </div>

</template>

<script>
export default {
    props:{
        technologies: Array
    }


}
</script>