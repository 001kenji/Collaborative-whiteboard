import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BoardView from '../views/BoardView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/board/:id',
    name: 'board',
    component: BoardView,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router