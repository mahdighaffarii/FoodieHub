// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue' // این کامپوننت را بعداً می‌سازیم
import { useAuthStore } from '../stores/authStore';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      // Lazy Loading: کامپوننت فقط زمانی لود می‌شود که به این مسیر برویم
      component: () => import('../views/LoginView.vue') 
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    // مسیرهای دیگر را در آینده اینجا اضافه خواهیم کرد

    {
      path: '/restaurants/:id', // <-- مسیر جدید
      name: 'restaurant-detail',
      component: () => import('../views/RestaurantDetailView.vue')
    },
    {
    path: '/my-profile',
    name: 'my-profile',
    component: () => import('../views/ProfileView.vue'),
    meta: { requiresAuth: true } // <-- این مسیر نیاز به لاگین دارد
  },
  {
    path: '/my-orders',
    name: 'my-orders',
    component: () => import('../views/OrderHistoryView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/wallet-history',
    name: 'wallet-history',
    component: () => import('../views/WalletHistoryView.vue'),
    meta: { requiresAuth: true }
  },
    {
    path: '/manager/dashboard',
    name: 'manager-dashboard',
    component: () => import('../views/ManagerDashboardView.vue'),
    meta: { requiresAuth: true, requiresManager: true } // نیاز به نقش مدیر
  },
  {
    path: '/manager/orders',
    name: 'manager-orders',
    component: () => import('../views/ManagerOrdersView.vue'),
    meta: { requiresAuth: true, requiresManager: true }
  },
  {
    path: '/manager/menu',
    name: 'manager-menu',
    component: () => import('../views/ManagerMenuView.vue'),
    meta: { requiresAuth: true, requiresManager: true }
  },
    {
    path: '/manager/reports',
    name: 'manager-reports',
    component: () => import('../views/ManagerReportsView.vue'),
    meta: { requiresAuth: true, requiresManager: true }
  },
    {
  path: '/manager/create-restaurant',
  name: 'manager-create-restaurant',
  component: () => import('../views/CreateRestaurantView.vue'),
  meta: { requiresAuth: true, requiresManager: true }
},
  ]
})

// src/router/index.js

// ... (بقیه کدها)

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();

  // مرحله ۱: صبر کن تا اطلاعات اولیه کاربر گرفته شود
  if (!authStore.isInitialized) {
    await authStore.fetchUserProfile();
  }

  const isLoggedIn = authStore.isLoggedIn;
  const user = authStore.user;
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresManager = to.matched.some(record => record.meta.requiresManager);

  // مرحله ۲: اگر کاربر لاگین نکرده
  if (!isLoggedIn) {
    if (requiresAuth) {
      // اگر صفحه نیاز به لاگین دارد، به صفحه لاگین بفرست
      return next({ name: 'login' });
    } else {
      // اگر نیاز به لاگین ندارد، اجازه عبور بده
      return next();
    }
  }

  // مرحله ۳: اگر کاربر لاگین کرده
  const isManager = user?.role === 'RESTAURANT_MANAGER';
  const hasRestaurant = !!user?.restaurant;

  // اگر می‌خواهد به صفحه لاگین یا ثبت‌نام برود، او را به خانه بفرست
  if (to.name === 'login' || to.name === 'register') {
    return next({ name: 'home' });
  }

  // اگر صفحه نیاز به مدیر دارد ولی کاربر مدیر نیست
  if (requiresManager && !isManager) {
    alert('شما دسترسی به این صفحه را ندارید.');
    return next({ name: 'home' });
  }

  // اگر کاربر مدیر است اما رستوران ندارد
  if (isManager && !hasRestaurant) {
    if (to.name !== 'manager-create-restaurant') {
      // اگر به صفحه‌ای غیر از "ایجاد رستوران" می‌رود، او را به آنجا بفرست
      return next({ name: 'manager-create-restaurant' });
    }
  }

  // اگر کاربر مدیر است و رستوران دارد
  if (isManager && hasRestaurant) {
    if (to.name === 'manager-create-restaurant') {
      // اگر به اشتباه به صفحه "ایجاد رستوران" می‌رود، او را به داشبورد بفرست
      return next({ name: 'manager-dashboard' });
    }
  }

  // اگر هیچ‌کدام از شرایط بالا برقرار نبود، اجازه عبور بده
  return next();
});

export default router;