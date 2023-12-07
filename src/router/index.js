import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import aboutView from '../views/AboutView.vue'
import tutorView from '../components/tutorView.vue'
import tutorView2 from '../components/tutorViewrefine.vue'
import dashView from '../components/dashboard.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: aboutView

    },
    {
      path: '/tutors',
      name: 'tutors',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: tutorView2

    },
    {
      path: '/dashboard',
      name: 'dashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: dashView

    },

  
  ]
})

export default router
