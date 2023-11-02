import { createRouter, createWebHistory } from 'vue-router'
import members from '../components/members.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/members',
      name: 'members',
      component: members
    },
  ]
})

export default router
