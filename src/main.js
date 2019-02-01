import Vue from 'vue';
import App from './App.vue';

// 引入vue-resource
import VueResource from 'vue-resource';
Vue.use(VueResource);

// 引入boostrap
import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue);

// 引入分离出来的路由模块
import router from './router/router.js';

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
