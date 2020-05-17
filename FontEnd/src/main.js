import Vue from 'vue'
import App from './App.vue'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import MintUI from 'mint-ui'

import 'swiper/css/swiper.css'
import 'mint-ui/lib/style.css'

Vue.config.productionTip = false

Vue.use(VueAwesomeSwiper)
Vue.use(MintUI)

new Vue({
  render: h => h(App),
}).$mount('#app')
