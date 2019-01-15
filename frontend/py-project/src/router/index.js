import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Home from '@/components/Home'
import test_api from '@/components/test_api'
import form from '@/components/form'
import Repay from '@/components/Repay'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,Login,Register
    },
    {
      path:'/login',
      name:'login',
      component:Login
    },
    {
      path:'/register',
      name:'register',
      component:Register
    },
    {
      path:'/home',
      name:'home',
      component:Home
    },
    {path:'/test_api',
    name:'test_api',
    component:test_api
    },
    {
      path:'/form',
      name:'form',
      component:form
    },
    {
      path:'/repay',
      name:'repay',
      component:Repay
    }
    
  ]
})
