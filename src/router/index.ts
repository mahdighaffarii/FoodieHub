import { createRouter, createWebHistory } from 'vue-router';
import RestaurantsListView from '@/views/RestaurantsListView.vue';
import RestaurantDetailView from '@/views/RestaurantDetailView.vue';
import CartView from '@/views/CartView.vue';
import CheckoutView from '@/views/CheckoutView.vue';
import OrdersHistoryView from '@/views/OrdersHistoryView.vue';
import LoginView from '@/views/LoginView.vue';
import { useAuthStore } from '@/store/auth.store';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: RestaurantsListView },
    { path: '/restaurants/:id', component: RestaurantDetailView },
    { path: '/cart', component: CartView },
    { path: '/checkout', component: CheckoutView, meta: { requiresAuth: true } },
    { path: '/orders', component: OrdersHistoryView, meta: { requiresAuth: true } },
    { path: '/login', component: LoginView },
  ],
});

router.beforeEach((to) => {
  const auth = useAuthStore();
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return { path: '/login', query: { redirect: to.fullPath } };
  }
});
export default router;
                