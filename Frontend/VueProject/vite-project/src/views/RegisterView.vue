<template>
  <div class="register-page">
    <div class="background-shapes">
      <div class="shape shape1"></div>
      <div class="shape shape2"></div>
      <div class="shape shape3"></div>
    </div>
    
    <div class="register-container">
      <!-- بخش بالایی کارت با لوگو -->
      <div class="register-header">
        <div class="logo-container">
          <img src="../assets/logo2.png" alt="FoodieHub Logo" class="logo">
          <div class="logo-glow"></div>
        </div>
        <h1 class="brand-name">FoodieHub</h1>
        <p class="tagline">به خانواده فودی‌هاب بپیوندید</p>
        <div class="welcome-message">
          <span>شروع یک تجربه غذایی فوق‌العاده!</span>
        </div>
      </div>

      <!-- فرم ثبت‌نام -->
      <form @submit.prevent="handleRegister" class="register-form">
        <div class="form-group" :class="{ 'focused': focusedField === 'email' }">
          <label for="email">
            <i class="icon-email">✉</i>
            ایمیل
          </label>
          <input 
            type="email" 
            id="email" 
            v-model="formData.email" 
            required 
            placeholder="ایمیل خود را وارد کنید"
            @focus="focusedField = 'email'"
            @blur="focusedField = ''"
          >
        </div>
        
        <div class="form-group" :class="{ 'focused': focusedField === 'username' }">
          <label for="username">
            <i class="icon-user">👤</i>
            نام کاربری
          </label>
          <input 
            type="text" 
            id="username" 
            v-model="formData.username" 
            required 
            placeholder="یک نام کاربری منحصر به فرد انتخاب کنید"
            @focus="focusedField = 'username'"
            @blur="focusedField = ''"
          >
        </div>
        
        <div class="form-group" :class="{ 'focused': focusedField === 'password' }">
          <label for="password">
            <i class="icon-lock">🔒</i>
            رمز عبور
          </label>
          <div class="password-input-container">
            <input 
              :type="showPassword ? 'text' : 'password'" 
              id="password" 
              v-model="formData.password" 
              required 
              placeholder="حداقل ۸ کاراکتر"
              @focus="focusedField = 'password'"
              @blur="focusedField = ''"
            >
            <button 
              type="button" 
              class="password-toggle" 
              @click="showPassword = !showPassword"
            >
              {{ showPassword ? '🙈' : '👁' }}
            </button>
          </div>
          <div class="password-strength" :class="passwordStrengthClass">
            <div class="strength-bar" :style="{ width: passwordStrength + '%' }"></div>
          </div>
        </div>
        
        <div class="form-group" :class="{ 'focused': focusedField === 'name' }">
          <label for="name">
            <i class="icon-person">🙋‍♂️</i>
            نام و نام خانوادگی
          </label>
          <input 
            type="text" 
            id="name" 
            v-model="formData.name" 
            required 
            placeholder="نام کامل خود را وارد کنید"
            @focus="focusedField = 'name'"
            @blur="focusedField = ''"
          >
        </div>
        
        <div class="form-group role-group" :class="{ 'focused': focusedField === 'role' }">
          <label for="role">
            <i class="icon-role">🎭</i>
            نوع کاربری
          </label>
          <select 
            id="role" 
            v-model="formData.role"
            @focus="focusedField = 'role'"
            @blur="focusedField = ''"
          >
            <option value="CUSTOMER">🍽️ مشتری (علاقه‌مند به سفارش غذا)</option>
            <option value="RESTAURANT_MANAGER">🏪 مدیر رستوران (صاحب کسب و کار)</option>
          </select>
        </div>
        
        <button type="submit" class="register-button" :disabled="isLoading">
          <span v-if="!isLoading">
            <i class="icon-arrow">🚀</i>
            عضویت در FoodieHub
          </span>
          <span v-else class="loading-text">
            <div class="spinner"></div>
            در حال ثبت‌نام...
          </span>
        </button>
      </form>

      <!-- لینک ورود -->
      <div class="login-link">
        <div class="divider">
          <span>یا</span>
        </div>
        <p>
          قبلاً حساب کاربری دارید؟ 
          <RouterLink to="/login" class="login-link-button">
            وارد شوید
            <i class="arrow-icon">←</i>
          </RouterLink>
        </p>
      </div>
      
      <!-- اعتماد و امنیت -->
      <div class="trust-badges">
        <div class="badge">
          <span class="badge-icon">🔐</span>
          <span>امن و محرمانه</span>
        </div>
        <div class="badge">
          <span class="badge-icon">⚡</span>
          <span>ثبت‌نام سریع</span>
        </div>
        <div class="badge">
          <span class="badge-icon">🎯</span>
          <span>تجربه شخصی‌سازی شده</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, computed } from 'vue';
import { useAuthStore } from '../stores/authStore';
import { RouterLink } from 'vue-router';

const authStore = useAuthStore();
const focusedField = ref('');
const showPassword = ref(false);
const isLoading = ref(false);

const formData = reactive({
  email: '',
  username: '',
  password: '',
  name: '',
  role: 'CUSTOMER',
});

const passwordStrength = computed(() => {
  const password = formData.password;
  let strength = 0;
  
  if (password.length >= 8) strength += 25;
  if (password.match(/[a-z]/)) strength += 25;
  if (password.match(/[A-Z]/)) strength += 25;
  if (password.match(/[0-9]/) || password.match(/[^a-zA-Z0-9]/)) strength += 25;
  
  return strength;
});

const passwordStrengthClass = computed(() => {
  if (passwordStrength.value < 25) return 'weak';
  if (passwordStrength.value < 50) return 'fair';
  if (passwordStrength.value < 75) return 'good';
  return 'strong';
});

const handleRegister = async () => {
  isLoading.value = true;
  try {
    await authStore.register({ ...formData });
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap');

.register-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: linear-gradient(135deg, #990505 0%, #6b0202 100%);
  position: relative;
  overflow: hidden;
  font-family: 'Vazirmatn', sans-serif;
}

.background-shapes {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  animation: float 6s ease-in-out infinite;
}

.shape1 {
  width: 200px;
  height: 200px;
  top: 10%;
  left: 10%;
  animation-delay: 0s;
}

.shape2 {
  width: 150px;
  height: 150px;
  top: 70%;
  right: 15%;
  animation-delay: 2s;
}

.shape3 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 70%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
}

.register-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 40px 35px;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 480px;
  text-align: center;
  position: relative;
  z-index: 1;
  border: 1px solid rgba(255, 255, 255, 0.2);
  animation: slideUp 0.8s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.register-header {
  margin-bottom: 35px;
}

.logo-container {
  position: relative;
  display: inline-block;
  margin-bottom: 15px;
}

.logo {
  width: 80px;
  height: auto;
  position: relative;
  z-index: 2;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1) rotate(5deg);
}

.logo-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, rgba(230, 57, 53, 0.3) 0%, transparent 70%);
  border-radius: 50%;
  z-index: 1;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.7; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
}

.brand-name {
  font-size: 28px;
  font-weight: 800;
  background: linear-gradient(135deg, #e53935, #ff7043);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.tagline {
  color: #666;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 10px;
}

.welcome-message {
  background: linear-gradient(135deg, #b00505, #860606);
  color: white;
  padding: 12px 20px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  display: inline-block;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  text-align: right;
  transition: all 0.3s ease;
  position: relative;
}

.form-group.focused {
  transform: translateY(-2px);
}

.form-group label {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin-bottom: 8px;
  font-weight: 600;
  color: #444;
  font-size: 15px;
  gap: 8px;
}

.form-group label i {
  font-size: 18px;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 16px 20px;
  border: 2px solid #e1e5e9;
  border-radius: 12px;
  box-sizing: border-box;
  font-size: 16px;
  font-family: 'Vazirmatn', sans-serif;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(5px);
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #e53935;
  box-shadow: 0 0 0 4px rgba(229, 57, 53, 0.1);
  background: white;
}

.form-group.focused input,
.form-group.focused select {
  border-color: #e53935;
  box-shadow: 0 0 0 4px rgba(229, 57, 53, 0.1);
}

.password-input-container {
  position: relative;
}

.password-toggle {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
  padding: 5px;
  border-radius: 4px;
  transition: background 0.2s ease;
}

.password-toggle:hover {
  background: rgba(0, 0, 0, 0.1);
}

.password-strength {
  height: 4px;
  background: #e1e5e9;
  border-radius: 2px;
  margin-top: 8px;
  overflow: hidden;
}

.strength-bar {
  height: 100%;
  border-radius: 2px;
  transition: all 0.3s ease;
}

.password-strength.weak .strength-bar { background: #f44336; }
.password-strength.fair .strength-bar { background: #ff9800; }
.password-strength.good .strength-bar { background: #2196f3; }
.password-strength.strong .strength-bar { background: #4caf50; }

.role-group select {
  cursor: pointer;
}

.register-button {
  width: 100%;
  padding: 18px;
  margin-top: 15px;
  background: linear-gradient(135deg, #e53935, #d32f2f);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 6px 20px rgba(229, 57, 53, 0.3);
  position: relative;
  overflow: hidden;
}

.register-button:hover:not(:disabled) {
  background: linear-gradient(135deg, #d32f2f, #b71c1c);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(229, 57, 53, 0.4);
}

.register-button:active {
  transform: translateY(0);
}

.register-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.loading-text {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.login-link {
  margin-top: 30px;
}

.divider {
  position: relative;
  margin: 25px 0;
}

.divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(to right, transparent, #ddd, transparent);
}

.divider span {
  background: white;
  color: #888;
  padding: 0 15px;
  font-size: 14px;
  position: relative;
}

.login-link p {
  color: #666;
  margin: 0;
}

.login-link-button {
  color: #e53935;
  font-weight: 700;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: all 0.3s ease;
  padding: 8px 12px;
  border-radius: 8px;
}

.login-link-button:hover {
  background: rgba(229, 57, 53, 0.1);
  transform: translateX(-3px);
}

.arrow-icon {
  transition: transform 0.3s ease;
}

.login-link-button:hover .arrow-icon {
  transform: translateX(-3px);
}

.trust-badges {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 30px;
  flex-wrap: wrap;
}

.badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  padding: 15px 10px;
  background: rgba(102, 126, 234, 0.1);
  border-radius: 12px;
  min-width: 100px;
  transition: transform 0.3s ease;
}

.badge:hover {
  transform: translateY(-3px);
}

.badge-icon {
  font-size: 24px;
}

.badge span:last-child {
  font-size: 12px;
  color: #666;
  font-weight: 500;
  text-align: center;
}

/* Responsive Design */
@media (max-width: 640px) {
  .register-page {
    padding: 15px;
  }
  
  .register-container {
    padding: 30px 25px;
  }
  
  .trust-badges {
    gap: 10px;
  }
  
  .badge {
    min-width: 80px;
    padding: 12px 8px;
  }
  
  .badge span:last-child {
    font-size: 11px;
  }
}

@media (max-width: 480px) {
  .brand-name {
    font-size: 24px;
  }
  
  .form-group input,
  .form-group select {
    padding: 14px 16px;
  }
  
  .register-button {
    padding: 16px;
    font-size: 16px;
  }
}
</style>