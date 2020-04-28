import Vue from 'vue'
import Router from 'vue-router'
// import Task  from '@/components/Task'
import App from '../App';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'App',
      component: App
    }
  ]
})
