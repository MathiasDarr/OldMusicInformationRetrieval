import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/Login'
import Register from './components/Register'
import Confirm from './components/Confirm'
// import Landing from './components/Landing'




// import MaestroTranscriptions from './components/music/piano/MaestroTranscriptions'
// import TranscriptionDetail from './components/music/guitar/TranscriptionDetail'

// import TranscriptionList from './components/music/TranscriptionList'

// import Transcriber from './components/music/Transcriber'
// import MusicProjectIntro from './components/music/MusicProjectIntro'
// import GuitarSet from './components/music/guitar/GuitarSet'
// import Transcription from './components/music/Transcription'


Vue.use(Router)

export default new Router({
  mode:'history',
  base: process.env.BASE_URL,
  routes: [

    {
      path: '/',
      component: Login
    },
    {
      path:'/login',
      component: Login
    },

    {
      path:'/register',
      name:'register',
      component: Register
    },

    {
      path:'/confirm',
      name:'confirm',
      component: Confirm
    },


    // {
    //   path: '/landing',
    //   component: Landing
    // },

    // {
    //   name: 'transcription',
    //   path: '/transcription/:id',
    //   component: Transcription

    // },

    // {
    //   path: '/transcriptions',
    //   component: TranscriptionList
    // },

    // {
    //   name:'transcription_detail',
    //   path: '/transcription_detail/:fileID/:title',
    //   component: TranscriptionDetail
    // },

    // {
    //   path: '/maestro',
    //   component: MaestroTranscriptions
    // },


    
    // {
    //   path:'/transcriber',
    //   component: Transcriber
    // },
    
    // {
    //   path:'/musiclanding',
    //   component: MusicProjectIntro
    // },

    // {
    //   path: '/transcriptions',
    //   component: TranscriptionList

    // },

    // {
    //   path:'/guitarset',
    //   component: GuitarSet
    // },

  ]
})
