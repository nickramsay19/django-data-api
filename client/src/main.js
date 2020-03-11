import Vue from 'vue'
import App from './App.vue'

// Setup Axios
import axios from '../node_modules/axios/dist/axios.min.js'
Vue.prototype.$axios = axios

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
