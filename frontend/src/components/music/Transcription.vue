<template>
  <v-container>
    <v-layout row>
    
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md10>

      </v-flex>

    </v-layout>
  </v-container>
</template>


<script>
export default {
    data(){
      return {
        items: [
            { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
            { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
            { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
            { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
            { title: 'Transcriptions', icon: 'mdi-help-box', route:'/transcriptions_list' },
          ],
      }
    }
}
</script>