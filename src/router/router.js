import Vue from 'vue'

// 引入vue-router
import VueRouter from 'vue-router'
Vue.use(VueRouter)

// 引入vuex中的store
import store from '../vuex/store.js'

// 引入组件
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Details from '../components/Details.vue'
import storage from '../model/storage.js'
// 配置路由
const routes = [
    { path: '/login', component: Login, name:'login', meta: { isLogin: false }},
    { path: '/home', component: Home, name: "home", meta: { isLogin: true } },
    { path: '/details', component: Details, name: "details", meta: { isLogin: true }},
    // {
    //     path: '/user', component: User,
    //     children: [
    //         { path: 'add', component: UserAdd },
    //         { path: 'list', component: UserList },
    //     ]
    // },
    // { path: '/news', component: News, name: "news" },
    // { path: '/content/:aid', component: Content, name: "content" }, // 动态路由
    // { path: '/pcontent', component: Pcontent }, // 动态路由,get跳转
    { path: '*', redirect: '/login' }, // 重定向到home
];

// 实例化VueRouter
const router = new VueRouter({
    mode: "history",
    routes
});

router.beforeEach((to, from, next)=>{
    var hasToken = storage.get("token");    
    if (hasToken){
        if(to.path == '/login'){
            next({
                path: 'home'
            })
        }else{         
            next();
        }
    }else{
        if(to.meta.isLogin == true){
            next({
                path: '/login',
            })
        }else{
            next();
        }
    }
})

router.afterEach(route => {
    window.scroll(0, 0);
});


export default router;
