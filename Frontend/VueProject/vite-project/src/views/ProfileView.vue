<!-- src/views/ProfileView.vue -->
<template>
  <div class="profile-page">
    <!-- Background Elements -->
    <div class="background-elements">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>

    <div class="profile-container">
      <!-- Profile Header -->
      <header class="profile-header">
        <div class="header-background">
          <div class="header-pattern"></div>
        </div>
        
        <div class="header-content">
          <div class="user-avatar">
            <div class="avatar-circle">
              <span class="avatar-text">
                {{ getUserInitials() }}
              </span>
            </div>
            <div class="avatar-status">
              <span class="status-dot"></span>
              <span class="status-text">آنلاین</span>
            </div>
          </div>
          
          <div class="user-details">
            <h1 class="profile-title">
              <span class="title-icon">👤</span>
              پروفایل کاربری
            </h1>
            
            <div class="welcome-message">
              <span class="welcome-text">خوش آمدید!</span>
              <span class="user-greeting">{{ getUserGreeting() }}</span>
            </div>
          </div>
        </div>
      </header>

      <!-- User Information Card -->
      <section class="user-info-section">
        <div class="section-header">
          <h2 class="section-title">
            <span class="title-icon">📋</span>
            اطلاعات حساب کاربری
          </h2>
        </div>
        
        <div v-if="authStore.user" class="user-info-card">
          <div class="info-grid">
            <div class="info-item">
              <div class="info-label">
                <i class="info-icon">✉️</i>
                <span>ایمیل</span>
              </div>
              <div class="info-value">
                {{ authStore.user.email }}
              </div>
            </div>
            
            <div class="info-item">
              <div class="info-label">
                <i class="info-icon">👤</i>
                <span>نام کاربری</span>
              </div>
              <div class="info-value">
                {{ authStore.user.username || 'تنظیم نشده' }}
              </div>
            </div>
            
            <div class="info-item">
              <div class="info-label">
                <i class="info-icon">🏷️</i>
                <span>نوع کاربری</span>
              </div>
              <div class="info-value">
                <span class="role-badge" :class="getRoleClass()">
                  {{ getRoleText() }}
                </span>
              </div>
            </div>
            
            <div class="info-item">
              <div class="info-label">
                <i class="info-icon">📅</i>
                <span>عضویت از</span>
              </div>
              <div class="info-value">
                {{ getJoinDate() }}
              </div>
            </div>
          </div>
          
          <div class="info-actions">
            <button class="edit-profile-btn">
              <i class="btn-icon">✏️</i>
              ویرایش پروفایل
            </button>
          </div>
        </div>

        <!-- Loading state for user info -->
        <div v-else class="loading-user-info">
          <div class="loading-spinner"></div>
          <p>در حال بارگذاری اطلاعات کاربری...</p>
        </div>
      </section>

      <!-- Navigation Menu -->
      <section class="navigation-section">
        <div class="section-header">
          <h2 class="section-title">
            <span class="title-icon">🧭</span>
            دسترسی سریع
          </h2>
        </div>
        
        <nav class="profile-nav">
          <RouterLink to="/my-orders" class="nav-item orders">
            <div class="nav-content">
              <div class="nav-icon">
                <span class="icon-bg"></span>
                <span class="icon-text">📋</span>
              </div>
              <div class="nav-details">
                <h3 class="nav-title">تاریخچه سفارشات</h3>
                <p class="nav-description">مشاهده سفارشات قبلی و پیگیری وضعیت</p>
              </div>
              <div class="nav-arrow">
                <i class="arrow-icon">←</i>
              </div>
            </div>
            <div class="nav-overlay"></div>
          </RouterLink>
          
          <RouterLink to="/wallet-history" class="nav-item wallet">
            <div class="nav-content">
              <div class="nav-icon">
                <span class="icon-bg"></span>
                <span class="icon-text">💳</span>
              </div>
              <div class="nav-details">
                <h3 class="nav-title">تاریخچه کیف پول</h3>
                <p class="nav-description">بررسی تراکنش‌ها و مانده حساب</p>
              </div>
              <div class="nav-arrow">
                <i class="arrow-icon">←</i>
              </div>
            </div>
            <div class="nav-overlay"></div>
          </RouterLink>
        </nav>
      </section>

      <!-- Quick Stats -->
      <section class="stats-section">
        <div class="section-header">
          <h2 class="section-title">
            <span class="title-icon">📊</span>
            آمار سریع
          </h2>
        </div>
        
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">🛒</div>
            <div class="stat-number">{{ mockStats.totalOrders }}</div>
            <div class="stat-label">کل سفارشات</div>
          </div>
          
          <div class="stat-card">
            <div class="stat-icon">💰</div>
            <div class="stat-number">{{ formatPrice(mockStats.totalSpent) }}</div>
            <div class="stat-label">کل خرید (تومان)</div>
          </div>
          
          <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <div class="stat-number">{{ mockStats.avgRating }}</div>
            <div class="stat-label">میانگین امتیاز</div>
          </div>
          
          <div class="stat-card">
            <div class="stat-icon">🍽️</div>
            <div class="stat-number">{{ mockStats.favoriteRestaurants }}</div>
            <div class="stat-label">رستوران مورد علاقه</div>
          </div>
        </div>
      </section>

      <!-- Account Actions -->
      <section class="actions-section">
        <div class="section-header">
          <h2 class="section-title">
            <span class="title-icon">⚙️</span>
            تنظیمات حساب
          </h2>
        </div>
        
        <div class="action-buttons">
          <button class="action-btn secondary">
            <i class="btn-icon">🔐</i>
            <span>تغییر رمز عبور</span>
          </button>
          
          <button class="action-btn secondary">
            <i class="btn-icon">🔔</i>
            <span>تنظیمات اعلانات</span>
          </button>
          
          <button class="action-btn secondary">
            <i class="btn-icon">📍</i>
            <span>آدرس‌های من</span>
          </button>
          
          <button class="action-btn danger" @click="handleLogout">
            <i class="btn-icon">🚪</i>
            <span>خروج از حساب</span>
          </button>
        </div>
      </section>
    </div>
  </div> <!-- <<-- تگ بسته نشده در اینجا اضافه شد -->
</template>

<script setup>
import { useAuthStore } from '../stores/authStore';
import { RouterLink, useRouter } from 'vue-router';
import { ref } from 'vue';

const authStore = useAuthStore();
const router = useRouter();

// Mock data for demonstration
const mockStats = ref({
  totalOrders: 24,
  totalSpent: 2450000,
  avgRating: 4.8,
  favoriteRestaurants: 8
});

const getUserInitials = () => {
  if (!authStore.user) return 'U';
  
  const email = authStore.user.email || '';
  const username = authStore.user.username || '';
  
  if (username) {
    return username.charAt(0).toUpperCase();
  }
  
  return email.charAt(0).toUpperCase();
};

const getUserGreeting = () => {
  const username = authStore.user?.username;
  const email = authStore.user?.email;
  
  if (username) {
    return username;
  }
  
  if (email) {
    return email.split('@')[0];
  }
  
  return 'کاربر عزیز';
};

const getRoleText = () => {
  const role = authStore.user?.role;
  
  switch (role) {
    case 'CUSTOMER':
      return 'مشتری';
    case 'RESTAURANT_MANAGER':
      return 'مدیر رستوران';
    default:
      return 'کاربر';
  }
};

const getRoleClass = () => {
  const role = authStore.user?.role;
  
  switch (role) {
    case 'CUSTOMER':
      return 'customer';
    case 'RESTAURANT_MANAGER':
      return 'manager';
    default:
      return 'default';
  }
};

const getJoinDate = () => {
  // Mock date - in real app, this would come from user data
  return 'آذر ۱۴۰۲';
};

const formatPrice = (price) => {
  return parseFloat(price).toLocaleString('fa-IR');
};

const handleLogout = async () => {
  if (confirm('آیا مطمئن هستید که می‌خواهید از حساب خود خارج شوید؟')) {
    await authStore.logout();
    router.push('/login');
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap');

.profile-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  font-family: 'Vazirmatn', sans-serif;
  position: relative;
  overflow-x: hidden;
}

.background-elements {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(220, 20, 60, 0.1), rgba(185, 28, 60, 0.1));
  animation: float 6s ease-in-out infinite;
}

.shape-1 {
  width: 200px;
  height: 200px;
  top: 10%;
  left: 5%;
  animation-delay: 0s;
}

.shape-2 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 10%;
  animation-delay: 2s;
}

.shape-3 {
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

.profile-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px;
  position: relative;
  z-index: 1;
}

/* Profile Header */
.profile-header {
  position: relative;
  background: linear-gradient(135deg, #dc143c 0%, #b91c3c 100%);
  color: white;
  border-radius: 25px;
  overflow: hidden;
  margin-bottom: 40px;
  box-shadow: 0 15px 40px rgba(220, 20, 60, 0.2);
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.header-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 15px,
    rgba(255, 255, 255, 0.05) 15px,
    rgba(255, 255, 255, 0.05) 30px
  );
}

.header-content {
  position: relative;
  z-index: 2;
  padding: 50px 40px;
  display: flex;
  align-items: center;
  gap: 40px;
}

.user-avatar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.avatar-circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: white;
  color: #dc143c;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 800;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  border: 4px solid rgba(255, 255, 255, 0.3);
}

.avatar-text {
  text-transform: uppercase;
}

.avatar-status {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #4ade80;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.user-details {
  flex: 1;
}

.profile-title {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
}

.title-icon {
  font-size: 2rem;
}

.welcome-message {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.welcome-text {
  font-size: 1.2rem;
  opacity: 0.9;
}

.user-greeting {
  font-size: 1.5rem;
  font-weight: 700;
}

/* Section Styling */
.section-header {
  margin-bottom: 30px;
}

.section-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #212529;
  display: flex;
  align-items: center;
  gap: 15px;
}

/* User Info Section */
.user-info-section {
  margin-bottom: 40px;
}

.user-info-card {
  background: white;
  border-radius: 20px;
  padding: 35px;
  box-shadow: 0 10px 30px rgba(220, 20, 60, 0.1);
  border: 2px solid transparent;
  transition: all 0.3s ease;
}

.user-info-card:hover {
  border-color: #dc143c;
  box-shadow: 0 15px 40px rgba(220, 20, 60, 0.15);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
  margin-bottom: 30px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.info-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  color: #666;
  font-weight: 600;
}

.info-icon {
  font-size: 1.2rem;
}

.info-value {
  font-size: 1.1rem;
  font-weight: 600;
  color: #212529;
  padding: 10px 15px;
  background: #f8f9fa;
  border-radius: 10px;
  border-left: 4px solid #dc143c;
}

.role-badge {
  display: inline-block;
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 700;
  text-transform: uppercase;
}

.role-badge.customer {
  background: #dc143c;
  color: white;
}

.role-badge.manager {
  background: #212529;
  color: white;
}

.role-badge.default {
  background: #6c757d;
  color: white;
}

.info-actions {
  display: flex;
  justify-content: center;
  padding-top: 20px;
  border-top: 1px solid #f0f0f0;
}

.edit-profile-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 15px 30px;
  background: #dc143c;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(220, 20, 60, 0.3);
}

.edit-profile-btn:hover {
  background: #b91c3c;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.4);
}

.loading-user-info {
  text-align: center;
  padding: 60px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(220, 20, 60, 0.1);
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f8f9fa;
  border-top: 3px solid #dc143c;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Navigation Section */
.navigation-section {
  margin-bottom: 40px;
}

.profile-nav {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
}

.nav-item {
  background: white;
  border-radius: 20px;
  padding: 30px;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 10px 30px rgba(220, 20, 60, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: 2px solid transparent;
}

.nav-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 50px rgba(220, 20, 60, 0.2);
  border-color: #dc143c;
}

.nav-content {
  display: flex;
  align-items: center;
  gap: 20px;
  position: relative;
  z-index: 2;
}

.nav-icon {
  position: relative;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #dc143c, #b91c3c);
  border-radius: 15px;
  opacity: 0.1;
  transition: all 0.3s ease;
}

.nav-item:hover .icon-bg {
  opacity: 0.2;
  transform: scale(1.1);
}

.icon-text {
  font-size: 2rem;
  position: relative;
  z-index: 2;
}

.nav-details {
  flex: 1;
}

.nav-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #212529;
  margin-bottom: 8px;
}

.nav-description {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.4;
  margin: 0;
}

.nav-arrow {
  font-size: 1.5rem;
  color: #dc143c;
  transition: transform 0.3s ease;
}

.nav-item:hover .nav-arrow {
  transform: translateX(-5px);
}

.nav-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(220, 20, 60, 0.05), rgba(185, 28, 60, 0.05));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.nav-item:hover .nav-overlay {
  opacity: 1;
}

/* Stats Section */
.stats-section {
  margin-bottom: 40px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.stat-card {
  background: white;
  border-radius: 15px;
  padding: 25px;
  text-align: center;
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.1);
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.stat-card:hover {
  transform: translateY(-5px);
  border-color: #dc143c;
  box-shadow: 0 12px 35px rgba(220, 20, 60, 0.15);
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 15px;
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #dc143c;
  margin-bottom: 8px;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
  font-weight: 500;
}

/* Actions Section */
.actions-section {
  margin-bottom: 40px;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 18px 25px;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  color: inherit;
}

.action-btn.secondary {
  background: white;
  color: #212529;
  border: 2px solid #e9ecef;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.action-btn.secondary:hover {
  background: #f8f9fa;
  border-color: #dc143c;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.15);
}

.action-btn.danger {
  background: #dc143c;
  color: white;
  box-shadow: 0 4px 15px rgba(220, 20, 60, 0.3);
}

.action-btn.danger:hover {
  background: #b91c3c;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.4);
}

.btn-icon {
  font-size: 1.2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .profile-container {
    padding: 20px 15px;
  }
  
  .header-content {
    flex-direction: column;
    text-align: center;
    padding: 40px 25px;
  }
  
  .profile-title {
    font-size: 2rem;
  }
  
  .info-grid {
    grid-template-columns: 1fr;
  }
  
  .profile-nav {
    grid-template-columns: 1fr;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .action-buttons {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .avatar-circle {
    width: 80px;
    height: 80px;
    font-size: 2rem;
  }
  
  .nav-content {
    flex-direction: column;
    text-align: center;
    gap: 15px;
  }
  
  .nav-arrow {
    transform: rotate(90deg);
  }
  
  .nav-item:hover .nav-arrow {
    transform: rotate(90deg) translateX(-5px);
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>