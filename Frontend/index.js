import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import Register from '../views/Register.vue'
import About from '../views/About.vue'
import Terms from '../views/Terms.vue'
import ContactUs from '../views/ContactUs.vue'



const routes = [
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/about', name: 'About', component: About },
  { path: '/forgot-password', name: 'ForgotPassword', component: ForgotPassword },
  { path: '/contact-us', name: 'ContactUs', component: ContactUs },
  { path: '/terms', name: 'Terms', component: Terms } 

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router