import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/result',
    name: 'result',
    component: () => import('../views/Result.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/user',
    name: 'user',
    component: () => import('../views/User.vue')
  },
  {
    path: '/detail',
    name: 'detail',
    component: () => import('../views/Detail.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router