import Vue from 'vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './App.vue'
import axios from 'axios'
import store from './store/store'
Vue.use(ElementUI)
Vue.use(router)

Vue.prototype.axios = axios;

new Vue({
    el: '#app',
    router,
    axios,
    store,
    render: h => h(App) // 为了在根元素#app下实例化一个App组件
})
