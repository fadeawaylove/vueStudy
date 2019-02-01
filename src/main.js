import Vue from 'vue';
import App from './App.vue';

// 引入element-ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// 引入vue-resource
import VueResource from 'vue-resource';
Vue.use(VueResource);

// 引入分离出来的路由模块
import router from './router/router.js';

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
