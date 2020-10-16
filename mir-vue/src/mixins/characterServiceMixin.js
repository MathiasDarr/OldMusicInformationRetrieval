import axios from 'axios'
export default{
    methods:{
        characterRequest: function(){
            axios.get('http://localhost:8083/characters/getall')
                  .then(response => {this.characters = response.data})
                  .catch((error) => console.log(error))
          },
    }
}