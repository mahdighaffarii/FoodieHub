import { defineStore } from 'pinia';
import apiClient from '../services/api';
import router from '../router';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('accessToken') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    isInitialized: false, // برای کنترل Route Guard
  }),

  getters: {
    isLoggedIn: (state) => !!state.accessToken,
  },

  actions: {
    async register(userData) {
      try {
        await apiClient.post('/accounts/register/', userData);
        await router.push('/login');
      } catch (error) {
        console.error('Registration failed:', error.response?.data);
        alert('ثبت‌نام ناموفق بود.');
      }
    },

    async login(credentials) {
      try {
        const response = await apiClient.post('/accounts/login/', credentials);
        this.accessToken = response.data.access;
        localStorage.setItem('accessToken', this.accessToken);
        
        // پس از لاگین موفق، بلافاصله اطلاعات کامل کاربر را می‌گیریم
        await this.fetchUserProfile();
        
        await router.push('/');
      } catch (error) {
        console.error('Login failed:', error.response?.data);
        alert('ورود ناموفق بود. ایمیل یا رمز عبور اشتباه است.');
      }
    },
    
    async fetchUserProfile() {
      // این تابع فقط یک بار در هر بار لود شدن برنامه باید اجرا شود
      if (this.isInitialized) return;

      if (localStorage.getItem('accessToken')) {
        try {
          const response = await apiClient.get('/accounts/profile/');
          this.user = response.data;
          localStorage.setItem('user', JSON.stringify(this.user));
        } catch (error) {
          console.error('Failed to fetch user profile, logging out:', error);
          this.logout(false); // لاگ اوت بدون هدایت به صفحه لاگین
        }
      }
      this.isInitialized = true; // در هر صورت، مقداردهی اولیه تمام شد
    },
    
   logout() {
    // ۱. تمام اطلاعات state را پاک می‌کنیم
    this.accessToken = null;
    this.user = null;
    this.isInitialized = false; // <-- مهم: اجازه می‌دهیم در لاگین بعدی دوباره مقداردهی شود

    // ۲. تمام اطلاعات را از localStorage پاک می‌کنیم
    localStorage.removeItem('accessToken');
    localStorage.removeItem('user');
    
    // ۳. (اختیاری اما بسیار موثر) کل state برنامه را ریست می‌کنیم
    // این کار باعث می‌شود store های دیگر (مثل cartStore) هم ریست شوند
    this.$reset();

    // ۴. کاربر را به صفحه لاگین هدایت می‌کنیم
    // استفاده از window.location.href باعث رفرش کامل صفحه می‌شود
    // و تمام وضعیت‌های باقی‌مانده را پاک می‌کند.
    window.location.href = '/login';
  }
  
  },
});