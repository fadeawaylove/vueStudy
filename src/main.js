import Vue from 'vue';
import App from './App.vue';

// 引入vue-resource
import VueResource from 'vue-resource';
Vue.use(VueResource);

// 引入boostrap
// import BootstrapVue from 'bootstrap-vue'
// Vue.use(BootstrapVue);

// 引入localStorage
import storage from './model/storage.js'

// 引入element-ui
import ElementUi from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUi);

// 引入分离出来的路由模块
import router from './router/router.js';

// 这里是拦截器
Vue.http.interceptors.push((request, next) => {
  //request.credentials = true; // 接口每次请求会跨域携带cookie
  //request.method= 'POST'; // 请求方式（get,post）
  var token = storage.get('token');
  if(token){
    request.headers.set('Authorization', 'Bearer ' + token) // 请求headers携带参数    
  } 
  // 先每次清除token 便于测试
  // storage.remove('token');

  next(function (response) {
    return response;
  });
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
