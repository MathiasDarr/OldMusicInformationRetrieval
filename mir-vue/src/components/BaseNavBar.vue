<template>
  <div>
    <v-card  height="400" flat>
      <v-navigation-drawer
        absolute >
        <v-list
          dense
          nav
          class="py-0">

              <v-list-item
                v-for="item in items"
                :key="item.title"
                link >
              <v-list-item-content @click="navigate(item.route)">

              <v-list-item-title>{{ item.title }}</v-list-item-title>

          </v-list-item-content>
         </v-list-item>
        </v-list>
      </v-navigation-drawer>

    </v-card>
  </div>
</template>

<script>

import router from '../router'


export default {
  created(){

  },
  props:{
    items:Array
  },

  methods:{
    navigate(route){
      if(route != this.$route.path){
        router.push(route)
      }
          
    }

  },

  data () {
      return {


      }
    },
  
}
</script>