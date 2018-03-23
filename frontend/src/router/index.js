import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/store'
import * as types from '../store/types'
import Index from '../components/index/index.vue'
import Class from '../components/class/classContent.vue'
import Admin from '../components/admin/admin.vue'
import Login from '../components/common/login.vue'
import Register from '../components/common/register.vue'
import home from '../components/admin/common/home.vue'
import goodsList from '../components/admin/common/goodsList.vue'
import pendingOrder from '../components/admin/common/pendingOrder.vue'
import about from '../components/admin/common/about.vue'
import add from '../components/admin/common/add.vue'
import userList from '../components/admin/common/userList.vue'
import classList from '../components/admin/common/classList.vue'
import logout from '../components/admin/common/logout.vue'
import goods from '../components/common/goods.vue'
import person from '../components/common/person.vue'
import userLogout from '../components/common/userLogout.vue'
import personHome from '../components/common/personHome.vue'
import order from '../components/common/order.vue'
import ordered from '../components/common/ordered.vue'
import express from '../components/common/express.vue'
import cart from '../components/common/cart.vue'
import pay from '../components/common/pay.vue'
Vue.use(VueRouter)
const routes = [
    {
        path: '/',
        name: 'index',
        component: Index
    },
    {
        path: '/class/:userId',
        name: 'class',
        component: Class
    },{
        path: '/pay',
        name: 'pay',
        component: pay
    },
    {
        path: '/goods/:goodsId',
        name: 'goods',
        component: goods
    },
    {
        path: '/cart',
        name: 'cart',
        component: cart
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/person',
        name: 'person',
        meta: {
            requireAuth: true
        },
        component: person,
        children: [
            {path: '/userLogout', component: userLogout},
            {path: '/personHome', component: personHome},
            {path: '/order', component: order},
            {path: '/ordered', component: ordered},
            {path: '/express', component: express},
        ]
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/admin',
        name: 'admin',
        meta: {
            requireAuth: true,
        },
        component: Admin,
        children: [
            {path: '', component: home},
            {path: '/home', component: home},
            {path: '/goodsList', component: goodsList},
            {path: '/pendingOrder', component: pendingOrder},
            {path: '/about', component: about},
            {path: '/add', component: add},
            {path: '/userList', component: userList},
            {path: '/classList', component: classList},
            {path: '/logout', component: logout}
        ]
    }
];
// 页面刷新时，重新赋值token
if (window.localStorage.getItem('token')) {
    store.commit(types.LOGIN, window.localStorage.getItem('token'))
}

const router = new VueRouter({
    routes
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(r => r.meta.requireAuth)) {
        if (store.state.token) {
            next()
        }
        else {
            next({
                path: '/login',
            })
        }
    }
    else {
        next();
    }
})

export default router;
// export default new Router({
//     routes: [{
//         path: '/',
//         name: 'index',
//         component: Index
//     },
//         {
//             path: '/class/:userId',
//             name: 'class',
//             component: Class
//         },
//         {
//             path:'/login',
//             name:'login',
//             component:Login
//         },
//         {
//             path:'/register',
//             name:'register',
//             component:Register
//         },
//         {
//             path: '/admin',
//             name: 'admin',
//             component: Admin,
//             meta:{
//                 requireAuth:true
//             },
//             children: [
//                 {path: '', component: home},
//                 {path: '/home', component: home},
//                 {path: '/goodsList', component: goodsList},
//                 {path: '/pendingOrder', component: pendingOrder},
//                 {path: '/about', component: about},
//             ]
//         }
//     ]
// })
