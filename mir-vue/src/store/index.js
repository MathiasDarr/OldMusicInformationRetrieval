import Vuex from 'vuex';
import Vue from 'vue';
import transcriptions from './modules/transcriptions';
import auth from './modules/auth'
import upload from './modules/upload'

// Load Vuex
Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    transcriptions,
    auth,
    upload
  }
});
