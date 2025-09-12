// src/stores/cartStore.js
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import apiClient from '../services/api';
import router from '../router';
import { useAuthStore } from './authStore';

export const useCartStore = defineStore('cart', () => {
  // State
  const items = ref([]); // لیستی از آیتم‌های سبد خرید
  const restaurantId = ref(null); // ID رستورانی که از آن خرید می‌کنیم

  // Getters (Computed Properties)
  const cartItemCount = computed(() => {
    return items.value.reduce((total, item) => total + item.quantity, 0);
  });
  const cartTotalPrice = computed(() => {
    return items.value.reduce((total, item) => total + (item.price * item.quantity), 0);
  });

  // Actions
  function addItem(foodItem) {
    // اگر سبد خرید خالی است یا آیتم جدید از همان رستوران قبلی است
    if (items.value.length === 0 || restaurantId.value === foodItem.restaurant) {
      restaurantId.value = foodItem.restaurant;
      const existingItem = items.value.find(item => item.id === foodItem.id);
      
      if (existingItem) {
        existingItem.quantity++;
      } else {
        items.value.push({ ...foodItem, quantity: 1 });
      }
      alert(`${foodItem.name} به سبد خرید اضافه شد.`);
    } else {
      // اگر کاربر سعی کند از یک رستوران دیگر غذا اضافه کند
      alert('شما فقط می‌توانید از یک رستوران در هر سفارش خرید کنید. لطفاً ابتدا سبد خرید خود را خالی کنید.');
    }
  }
  
  function removeItem(foodItemId) {
    const index = items.value.findIndex(item => item.id === foodItemId);
    if (index !== -1) {
      items.value.splice(index, 1);
    }
    if (items.value.length === 0) {
        restaurantId.value = null;
    }
  }

  function clearCart() {
    items.value = [];
    restaurantId.value = null;
  }

  async function checkout() {
    const authStore = useAuthStore();
    if (!authStore.isLoggedIn) {
      alert('برای ثبت سفارش، لطفاً ابتدا وارد شوید.');
      router.push('/login');
      return;
    }

    if (items.value.length === 0) {
      alert('سبد خرید شما خالی است.');
      return;
    }

    const orderData = {
      restaurant_id: restaurantId.value,
      items: items.value.map(item => ({
        food_item_id: item.id,
        quantity: item.quantity,
      })),
    };

    try {
      await apiClient.post('/orders/create/', orderData);
      alert('سفارش شما با موفقیت ثبت شد!');
      clearCart();
      // کاربر را به صفحه تاریخچه سفارشات هدایت می‌کنیم (این صفحه را بعداً می‌سازیم)
      router.push('/my-orders'); 
    } catch (error) {
      console.error('Checkout failed:', error.response?.data);
      alert(`ثبت سفارش ناموفق بود: ${error.response?.data?.error || 'خطای سرور'}`);
    }
  }

  return { items, restaurantId, cartItemCount, cartTotalPrice, addItem, removeItem, clearCart, checkout };
});