/* eslint-disable */

import axios from 'axios';


const state = {
  tweets: [],

};

const getters = {
  getUploadedFile: state => state.tweets,

};

const actions = {  
    async uploadFile({commit}, fd){
      console.log("hooray")        
      const api_url = window.__runtime_configuration.api+'upload'
        axios.post(api_url, fd).then((response) => {
          console.log(response)
        }, (error) => {
          
        console.log(error);
      });
    } 
};

const mutations = {
    setUploadedFile: (state, tweets) => (state.tweets = tweets)
};

export default {
  state,
  getters,
  actions,
  mutations
};
