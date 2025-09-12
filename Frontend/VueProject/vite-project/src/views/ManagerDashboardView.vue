<template>
  <div class="manager-dashboard">
    <!-- Header Section -->
    <div class="dashboard-header">
      <div class="welcome-section">
        <div class="manager-icon">👨‍💼</div>
        <h1 class="dashboard-title">پنل مدیریت رستوران</h1>
        <p class="welcome-text">خوش آمدید! از این پنل می‌توانید تمامی بخش‌های رستوران را مدیریت کنید</p>
      </div>
    </div>

    <!-- Navigation Cards -->
    <div class="navigation-section">
      <h2 class="section-title">دسترسی سریع</h2>
      <div class="nav-cards">
        <RouterLink to="/manager/orders" class="nav-card orders-card">
          <div class="card-icon">📋</div>
          <div class="card-content">
            <h3 class="card-title">مدیریت سفارشات</h3>
            <p class="card-description">مشاهده و پردازش سفارشات دریافتی</p>
          </div>
          <div class="card-arrow">←</div>
        </RouterLink>

        <RouterLink to="/manager/menu" class="nav-card menu-card">
          <div class="card-icon">🍽️</div>
          <div class="card-content">
            <h3 class="card-title">مدیریت منو</h3>
            <p class="card-description">افزودن، ویرایش و حذف غذاها</p>
          </div>
          <div class="card-arrow">←</div>
        </RouterLink>

        <RouterLink to="/manager/reports" class="nav-card reports-card">
          <div class="card-icon">📊</div>
          <div class="card-content">
            <h3 class="card-title">گزارشات فروش</h3>
            <p class="card-description">مشاهده آمار و گزارشات مالی</p>
          </div>
          <div class="card-arrow">←</div>
        </RouterLink>
      </div>
    </div>

    <!-- Restaurant Image Section -->
    <div class="restaurant-showcase">
      <div class="image-container">
        <img 
          src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2074&q=80" 
          alt="رستوران زیبا"
          class="restaurant-image"
        />
        <div class="image-overlay">
          <h3 class="overlay-title">رستوران شما، تجربه‌ای بی‌نظیر</h3>
          <p class="overlay-text">ما با افتخار بهترین غذاها و خدمات را به مشتریانمان ارائه می‌دهیم</p>
        </div>
      </div>
    </div>

    <!-- Stats Preview -->
    <div class="stats-preview">
      <div class="stat-item">
        <div class="stat-icon">🍕</div>
        <div class="stat-number">150+</div>
        <div class="stat-label">غذای متنوع</div>
      </div>
      <div class="stat-item">
        <div class="stat-icon">⭐</div>
        <div class="stat-number">4.8</div>
        <div class="stat-label">امتیاز مشتریان</div>
      </div>
      <div class="stat-item">
        <div class="stat-icon">🚚</div>
        <div class="stat-number">24/7</div>
        <div class="stat-label">ارسال سریع</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap");

/* Base Styles */
.manager-dashboard {
  min-height: 100vh;
  background: #ffffff;
  color: #000000;
  font-family: "Vazirmatn", sans-serif;
  padding: 40px 20px;
  line-height: 1.6;
}

/* Header Section */
.dashboard-header {
  text-align: center;
  padding: 60px 20px;
  border: 3px solid #dc143c;
  border-radius: 20px;
  background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
  box-shadow: 0 8px 32px rgba(220, 20, 60, 0.1);
  margin-bottom: 40px;
  position: relative;
  overflow: hidden;
}

.dashboard-header::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(220, 20, 60, 0.03) 0%, transparent 70%);
  pointer-events: none;
}

.manager-icon {
  font-size: 5rem;
  margin-bottom: 20px;
  display: inline-block;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
}

.dashboard-title {
  font-size: 3.5rem;
  font-weight: 800;
  color: #dc143c;
  margin: 0 0 16px 0;
  text-shadow: 0 2px 4px rgba(220, 20, 60, 0.1);
}

.welcome-text {
  font-size: 1.3rem;
  font-weight: 400;
  color: #666666;
  margin: 0;
  max-width: 600px;
  margin: 0 auto;
}

/* Navigation Section */
.navigation-section {
  margin-bottom: 60px;
}

.section-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #dc143c;
  text-align: center;
  margin: 0 0 40px 0;
}

.nav-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
}

.nav-card {
  display: flex;
  align-items: center;
  padding: 32px;
  border: 3px solid #dc143c;
  border-radius: 16px;
  background: #ffffff;
  text-decoration: none;
  color: #000000;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(220, 20, 60, 0.08);
  position: relative;
  overflow: hidden;
}

.nav-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(220, 20, 60, 0.05), transparent);
  transition: left 0.5s ease;
}

.nav-card:hover::before {
  left: 100%;
}

.nav-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(220, 20, 60, 0.15);
  border-color: #dc143c;
}

.card-icon {
  font-size: 3rem;
  margin-left: 20px;
  flex-shrink: 0;
}

.card-content {
  flex: 1;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #dc143c;
  margin: 0 0 8px 0;
}

.card-description {
  font-size: 1.1rem;
  color: #666666;
  margin: 0;
}

.card-arrow {
  font-size: 1.5rem;
  color: #dc143c;
  font-weight: bold;
  margin-right: 16px;
  transition: transform 0.3s ease;
}

.nav-card:hover .card-arrow {
  transform: translateX(-5px);
}

/* Restaurant Showcase */
.restaurant-showcase {
  margin-bottom: 40px;
}

.image-container {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  border-radius: 20px;
  overflow: hidden;
  border: 3px solid #dc143c;
  box-shadow: 0 12px 40px rgba(220, 20, 60, 0.15);
}

.restaurant-image {
  width: 100%;
  height: 500px;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.image-container:hover .restaurant-image {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
  color: #ffffff;
  padding: 40px;
  text-align: center;
}

.overlay-title {
  font-size: 2.2rem;
  font-weight: 700;
  margin: 0 0 12px 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.overlay-text {
  font-size: 1.2rem;
  margin: 0;
  opacity: 0.9;
  max-width: 600px;
  margin: 0 auto;
}

/* Stats Preview */
.stats-preview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  max-width: 900px;
  margin: 0 auto;
}

.stat-item {
  text-align: center;
  padding: 32px 24px;
  border: 3px solid #dc143c;
  border-radius: 16px;
  background: #ffffff;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(220, 20, 60, 0.08);
}

.stat-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(220, 20, 60, 0.12);
}

.stat-icon {
  font-size: 3rem;
  margin-bottom: 16px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #dc143c;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 1.1rem;
  color: #666666;
  font-weight: 500;
}

/* Responsive Design */
@media (max-width: 768px) {
  .manager-dashboard {
    padding: 24px 16px;
  }

  .dashboard-header {
    padding: 40px 20px;
  }

  .dashboard-title {
    font-size: 2.5rem;
  }

  .welcome-text {
    font-size: 1.1rem;
  }

  .nav-cards {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .nav-card {
    padding: 24px;
  }

  .card-title {
    font-size: 1.3rem;
  }

  .card-description {
    font-size: 1rem;
  }

  .restaurant-image {
    height: 300px;
  }

  .overlay-title {
    font-size: 1.8rem;
  }

  .overlay-text {
    font-size: 1rem;
  }

  .stats-preview {
    grid-template-columns: 1fr;
  }

  .stat-item {
    padding: 24px 20px;
  }
}

@media (max-width: 480px) {
  .dashboard-title {
    font-size: 2rem;
  }

  .section-title {
    font-size: 1.8rem;
  }

  .nav-card {
    padding: 20px;
    flex-direction: column;
    text-align: center;
  }

  .card-icon {
    margin-left: 0;
    margin-bottom: 16px;
  }

  .card-arrow {
    margin-right: 0;
    margin-top: 16px;
  }

  .restaurant-image {
    height: 250px;
  }

  .image-overlay {
    padding: 24px;
  }
}
</style>