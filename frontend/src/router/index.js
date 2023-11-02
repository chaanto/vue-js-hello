import { createRouter, createWebHistory } from 'vue-router'
import members from '../components/members.vue'
import Books from '../components/Books.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/members',
      name: 'members',
      component: members
    },
    {
      path: '/books',
      name: 'books',
      component: Books
    },  
  ]
})

export default router
