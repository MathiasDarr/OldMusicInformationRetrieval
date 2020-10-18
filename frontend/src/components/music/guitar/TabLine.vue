<template>
  <v-container>
    <div id="tab">
    </div>
  </v-container>
</template>

<script>
/* eslint-disable */

import Vex from 'vexflow';
// import { mapGetters, mapActions } from "vuex";

var GuitarMidiFret = [
    [40, 41,42,43,43,44,45,46,47,48,49,50,51,52,53,54,55],  
    [45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60],
    [50,51,52,53,54,55,56,57,58, 59,60,61,62,63,64],
    [55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70],
    [59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74],
    [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
       
]


export default {

    props:{
        notes:Array
    },

    data () {
      return {
       
      }
    },    
    
    created(){
        // console.log("NOTES " + this.notes)
    },

    mounted(){
        while(this.notes[this.notes.length-1] == undefined){
          this.notes.pop()
        }
        
        const VF = Vex.Flow;
        var div = document.getElementById("tab")
        var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);
        renderer.resize(1500, 130);
        var context = renderer.getContext();

        var notesArray = []
        // console.log(notesArray)
        var i =0
        while(i< this.notes.length){
        
          var positions = []
          var j =i
          while(this.notes[j]!= undefined && this.notes[j][1] == this.notes[i][1]){
            
            // console.log("this.notes[j] " + this.notes[j][3] )
            // var fret = GuitarMidiFret[Math.floor(this.notes[j][3])]  //.indexOf(this.notes[j][2])
            // positions.push({str: Math.floor(this.notes[j][3])+1, fret: fret})
            // j+=1
          }
          var tabnote = new VF.TabNote({positions: positions, duration: "q"})
          notesArray.push(tabnote)   
          i=j
        }

        var stave = new VF.TabStave(10, 0, 1400);
        stave.addClef("tab").setContext(context).draw();

        VF.Formatter.FormatAndDraw(context, stave, notesArray);

    },
    computed: {

    }
}
</script>