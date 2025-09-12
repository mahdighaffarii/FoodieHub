<template>
  <header>
    <nav>
      <RouterLink to="/">صفحه اصلی</RouterLink>

      <div class="nav-right">
        <div class="cart-icon" @click="showCart = !showCart">
          🛒
          <span v-if="cartStore.cartItemCount > 0" class="cart-badge">
            {{ cartStore.cartItemCount }}
          </span>
        </div>

        <template v-if="authStore.isLoggedIn && authStore.user">
          <RouterLink
            v-if="authStore.user.role === 'RESTAURANT_MANAGER'"
            to="/manager/dashboard"
          >
            پنل مدیریت
          </RouterLink>
          <RouterLink to="/my-profile">پروفایل من</RouterLink>
          <a @click="authStore.logout()" href="#" class="logout-link">خروج</a>
        </template>
        <template v-else>
          <RouterLink to="/login">ورود</RouterLink>
          <RouterLink to="/register">ثبت‌نام</RouterLink>
        </template>
      </div>
    </nav>
  </header>

  <ShoppingCart v-if="showCart" />

  <RouterView />
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useAuthStore } from './stores/authStore';
import { useCartStore } from './stores/cartStore';
import ShoppingCart from './components/ShoppingCart.vue';

const authStore = useAuthStore();
const cartStore = useCartStore();
const showCart = ref(false);
</script>

<style scoped>
/* نوار ناوبری اصلی */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #ffffff; /* زمینه سفید */
  border-bottom: 3px solid #d32f2f; /* خط قرمز پررنگ زیر منو */
  font-size: 16px;
}

/* بخش سمت راست */
.nav-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

/* لینک‌ها */
a,
.router-link-active,
.router-link-exact-active {
  color: #000000; /* متن سیاه */
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

a:hover,
.router-link-active:hover,
.router-link-exact-active:hover {
  color: #d32f2f; /* هاور قرمز پررنگ */
}

/* آیکون سبد خرید */
.cart-icon {
  position: relative;
  cursor: pointer;
  font-size: 18px;
  color: #000000;
  transition: color 0.2s ease;
}
.cart-icon:hover {
  color: #d32f2f;
}

/* نشانگر تعداد آیتم‌ها */
.cart-badge {
  position: absolute;
  top: -8px;
  right: -12px;
  background-color: #d32f2f; /* قرمز پررنگ */
  color: white;
  border-radius: 50%;
  padding: 2px 6px;
  font-size: 10px;
  font-weight: bold;
}

/* لینک خروج */
.logout-link {
  cursor: pointer;
}
</style>
