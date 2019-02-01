import Vue from 'vue'


// 引入vue-router
import VueRouter from 'vue-router'
Vue.use(VueRouter)

// 引入组件
import Login from '../components/Login.vue'

// 配置路由
const routes = [
    { path: '/login', component: Login},
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
    // { path: '*', redirect: '/home' }, // 重定向到home
];

// 实例化VueRouter
const router = new VueRouter({
    mode: "history",
    routes
});

export default router;
