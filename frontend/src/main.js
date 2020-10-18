import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import store from './store';
Vue.config.productionTip = false
import router from './router.js'
import cognitoAuth from './cognito'





new Vue({
  vuetify,
  store,
  router,
  cognitoAuth,
  render: h => h(App),
  
}).$mount('#app')
