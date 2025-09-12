<template>
  <div class="login-page">
    <div class="background-animation">
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
      </div>
    </div>
    
    <div class="login-container">
      <!-- بخش بالایی کارت با لوگو -->
      <div class="login-header">
        <div class="logo-wrapper">
          <img src="../assets/logo2.png" alt="FoodieHub Logo" class="logo">
          <div class="logo-ring"></div>
        </div>
        <h1 class="brand-name">FoodieHub</h1>
        <p class="welcome-text">خوش آمدید!</p>
        <div class="tagline">
          <span class="highlight">به دنیای طعم‌های بی‌نظیر</span> وارد شوید
        </div>
      </div>

      <!-- فرم ورود -->
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group" :class="{ 'focused': focusedField === 'email', 'has-value': email }">
          <label for="email">
            <i class="icon">👤</i>
            ایمیل یا نام کاربری
          </label>
          <div class="input-wrapper">
            <input 
              type="email" 
              id="email" 
              v-model="email" 
              required 
              placeholder="ایمیل خود را وارد کنید"
              @focus="focusedField = 'email'"
              @blur="focusedField = ''"
            >
            <div class="input-highlight"></div>
          </div>
        </div>
        
        <div class="form-group" :class="{ 'focused': focusedField === 'password', 'has-value': password }">
          <label for="password">
            <i class="icon">🔐</i>
            رمز عبور
          </label>
          <div class="input-wrapper">
            <input 
              :type="showPassword ? 'text' : 'password'" 
              id="password" 
              v-model="password" 
              required 
              placeholder="رمز عبور خود را وارد کنید"
              @focus="focusedField = 'password'"
              @blur="focusedField = ''"
            >
            <button 
              type="button" 
              class="password-toggle" 
              @click="showPassword = !showPassword"
              tabindex="-1"
            >
              <span v-if="showPassword">🙈</span>
              <span v-else>👁</span>
            </button>
            <div class="input-highlight"></div>
          </div>
        </div>

        <!-- گزینه‌های اضافی -->
        <div class="form-options">
          <label class="remember-me">
            <input type="checkbox" v-model="rememberMe">
            <span class="checkmark"></span>
            مرا به خاطر بسپار
          </label>
          <a href="#" class="forgot-password">فراموشی رمز عبور؟</a>
        </div>

        <button type="submit" class="login-button" :disabled="isLoading" :class="{ 'loading': isLoading }">
          <span v-if="!isLoading" class="button-content">
            <i class="login-icon">🚀</i>
            ورود به FoodieHub
          </span>
          <span v-else class="loading-content">
            <div class="spinner"></div>
            در حال ورود...
          </span>
        </button>
      </form>

      <!-- جداکننده -->
      <div class="divider">
        <span>یا</span>
      </div>

      <!-- لینک ثبت‌نام -->
      <div class="signup-section">
        <p class="signup-text">تازه‌وارد هستید؟</p>
        <RouterLink to="/register" class="signup-button">
          <span class="signup-icon">✨</span>
          همین الان ثبت‌نام کنید
          <i class="arrow">←</i>
        </RouterLink>
      </div>

      <!-- ویژگی‌های برجسته -->
      <div class="features">
        <div class="feature">
          <span class="feature-icon">⚡</span>
          <span class="feature-text">ورود سریع</span>
        </div>
        <div class="feature">
          <span class="feature-icon">🔒</span>
          <span class="feature-text">امنیت بالا</span>
        </div>
        <div class="feature">
          <span class="feature-icon">🍽️</span>
          <span class="feature-text">هزاران رستوران</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/authStore';
import { RouterLink } from 'vue-router';

const authStore = useAuthStore();
const email = ref('');
const password = ref('');
const focusedField = ref('');
const showPassword = ref(false);
const rememberMe = ref(false);
const isLoading = ref(false);

const handleLogin = async () => {
  isLoading.value = true;
  try {
    await authStore.login({ 
      email: email.value, 
      password: password.value,
      rememberMe: rememberMe.value
    });
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap');

.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #8f0202 0%, #570202 100%);
  font-family: 'Vazirmatn', sans-serif;
  position: relative;
  overflow: hidden;
  padding: 20px;
}

.background-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.floating-shapes {
  position: relative;
  width: 100%;
  height: 100%;
}

.shape {
  position: absolute;
  border-radius: 50%;
  background: rgba(6, 6, 6, 0.1);
  animation: float 8s ease-in-out infinite;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.shape-2 {
  width: 80px;
  height: 80px;
  top: 60%;
  right: 15%;
  animation-delay: 2s;
}

.shape-3 {
  width: 60px;
  height: 60px;
  bottom: 30%;
  left: 70%;
  animation-delay: 4s;
}

.shape-4 {
  width: 100px;
  height: 100px;
  top: 80%;
  left: 20%;
  animation-delay: 6s;
}

@keyframes float {
  0%, 100% { 
    transform: translateY(0px) translateX(0px) rotate(0deg); 
    opacity: 0.7;
  }
  25% { 
    transform: translateY(-20px) translateX(10px) rotate(5deg); 
    opacity: 1;
  }
  50% { 
    transform: translateY(-10px) translateX(-5px) rotate(-3deg); 
    opacity: 0.8;
  }
  75% { 
    transform: translateY(-30px) translateX(-10px) rotate(8deg); 
    opacity: 0.9;
  }
}

.login-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 45px 40px;
  border-radius: 28px;
  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 450px;
  text-align: center;
  position: relative;
  z-index: 1;
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: slideIn 0.8s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(40px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.login-header {
  margin-bottom: 40px;
}

.logo-wrapper {
  position: relative;
  display: inline-block;
  margin-bottom: 20px;
}

.logo {
  width: 90px;
  height: auto;
  position: relative;
  z-index: 2;
  transition: all 0.4s ease;
  filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.15));
}

.logo:hover {
  transform: scale(1.1) rotate(-5deg);
}

.logo-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 110px;
  height: 110px;
  border: 3px solid rgba(230, 57, 53, 0.3);
  border-radius: 50%;
  z-index: 1;
  animation: rotate 4s linear infinite;
}

@keyframes rotate {
  from { transform: translate(-50%, -50%) rotate(0deg); }
  to { transform: translate(-50%, -50%) rotate(360deg); }
}

.brand-name {
  font-size: 32px;
  font-weight: 800;
  background: linear-gradient(135deg, #e53935, #ff7043);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 10px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.welcome-text {
  font-size: 18px;
  color: #666;
  margin-bottom: 15px;
  font-weight: 500;
}

.tagline {
  font-size: 15px;
  color: #777;
  line-height: 1.4;
}

.highlight {
  color: #e53935;
  font-weight: 600;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.form-group {
  text-align: right;
  position: relative;
}

.form-group label {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin-bottom: 10px;
  font-weight: 600;
  color: #555;
  font-size: 16px;
  gap: 10px;
}

.icon {
  font-size: 20px;
}

.input-wrapper {
  position: relative;
}

.form-group input {
  width: 100%;
  padding: 18px 20px;
  border: 2px solid #e1e5e9;
  border-radius: 14px;
  box-sizing: border-box;
  font-size: 16px;
  font-family: 'Vazirmatn', sans-serif;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(5px);
}

.form-group input:focus {
  outline: none;
  border-color: #e53935;
  background: white;
  box-shadow: 0 0 0 4px rgba(229, 57, 53, 0.1);
}

.form-group.focused .input-highlight {
  transform: scaleX(1);
}

.input-highlight {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(135deg, #e53935, #ff7043);
  transform: scaleX(0);
  transition: transform 0.3s ease;
  border-radius: 0 0 14px 14px;
}

.password-toggle {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  padding: 8px;
  border-radius: 8px;
  transition: all 0.3s ease;
  z-index: 2;
}

.password-toggle:hover {
  background: rgba(229, 57, 53, 0.1);
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
  font-size: 14px;
}

.remember-me {
  display: flex;
  align-items: center;
  cursor: pointer;
  gap: 8px;
}

.remember-me input {
  display: none;
}

.checkmark {
  width: 18px;
  height: 18px;
  border: 2px solid #ddd;
  border-radius: 4px;
  position: relative;
  transition: all 0.3s ease;
}

.remember-me input:checked + .checkmark {
  background: #e53935;
  border-color: #e53935;
}

.remember-me input:checked + .checkmark::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.forgot-password {
  color: #e53935;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
}

.forgot-password:hover {
  text-decoration: underline;
  color: #d32f2f;
}

.login-button {
  width: 100%;
  padding: 20px;
  margin-top: 15px;
  background: linear-gradient(135deg, #e53935, #d32f2f);
  color: white;
  border: none;
  border-radius: 14px;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(229, 57, 53, 0.3);
  position: relative;
  overflow: hidden;
}

.login-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.login-button:hover:not(:disabled) {
  background: linear-gradient(135deg, #d32f2f, #b71c1c);
  transform: translateY(-2px);
  box-shadow: 0 12px 35px rgba(229, 57, 53, 0.4);
}

.login-button:hover:not(:disabled)::before {
  left: 100%;
}

.login-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.button-content,
.loading-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.login-icon {
  font-size: 20px;
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

.divider {
  position: relative;
  margin: 30px 0;
  text-align: center;
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
  color: #999;
  padding: 0 20px;
  font-size: 14px;
  font-weight: 500;
}

.signup-section {
  text-align: center;
}

.signup-text {
  color: #666;
  margin-bottom: 15px;
  font-size: 15px;
}

.signup-button {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 15px 25px;
  background: linear-gradient(135deg, #940303, #8f0303);
  color: white;
  text-decoration: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 16px;
  transition: all 0.3s ease;
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
}

.signup-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(143, 4, 4, 0.4);
}

.signup-icon {
  font-size: 18px;
}

.arrow {
  transition: transform 0.3s ease;
}

.signup-button:hover .arrow {
  transform: translateX(-5px);
}

.features {
  display: flex;
  justify-content: center;
  gap: 25px;
  margin-top: 30px;
  flex-wrap: wrap;
}

.feature {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 15px;
  background: rgba(102, 126, 234, 0.1);
  border-radius: 12px;
  transition: all 0.3s ease;
  min-width: 90px;
}

.feature:hover {
  transform: translateY(-3px);
  background: rgba(102, 126, 234, 0.15);
}

.feature-icon {
  font-size: 24px;
}

.feature-text {
  font-size: 12px;
  color: #666;
  font-weight: 500;
  text-align: center;
}

/* Responsive Design */
@media (max-width: 640px) {
  .login-page {
    padding: 15px;
  }
  
  .login-container {
    padding: 35px 25px;
  }
  
  .features {
    gap: 15px;
  }
  
  .feature {
    min-width: 70px;
    padding: 12px;
  }
  
  .form-options {
    flex-direction: column;
    gap: 15px;
    align-items: center;
  }
}

@media (max-width: 480px) {
  .brand-name {
    font-size: 26px;
  }
  
  .form-group input {
    padding: 16px 18px;
  }
  
  .login-button {
    padding: 18px;
    font-size: 16px;
  }
  
  .signup-button {
    padding: 12px 20px;
    font-size: 14px;
  }
}
</style>