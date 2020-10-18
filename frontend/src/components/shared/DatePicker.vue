<template>
  <v-layout row wrap>
    <v-menu
      v-model="fromDateMenu"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="290px"
    >
      <template v-slot:activator="{ on }">
        <v-text-field
          :label="label"
          readonly
          :value="fromDateDisp"
          v-on="on"
        ></v-text-field>
      </template>
      <v-date-picker
        locale="en-in"
        :min="minDate"
        :max="maxDate"
        v-model="dateVal"
        no-title
        @input="fromDateMenu = false"
      ></v-date-picker>
    </v-menu>
  </v-layout>

</template>

<script>
  export default {
    props:{
        label:String,
        fromDateVal:String,
        start: Boolean
    },
    data() {
      return {
        fromDateMenu: false,
        dateVal: this.fromDateVal,
        // fromDateVal: "2014-",

        minDate: "2014-01-01",
        maxDate: "2020-01-01"
      };
    },
    computed: {
      fromDateDisp() {

        if(this.start){
          this.$emit('clicked', this.dateVal, true)
          console.log("Start " + this.dateVal)
        }else{
          this.$emit('clicked', this.dateVal, false)
        }


        return this.dateVal;

      }
    }
  };
</script>
