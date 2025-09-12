<!-- src/views/HomeView.vue -->
<template>
  <main class="home-view">
    <!-- Header Section -->
    <section class="hero-section">
      <div class="hero-content">
        <div class="hero-text">
          <h1 class="main-title">
            <span class="title-highlight">🍽️ FoodieHub</span>
            <span class="title-subtitle">رستوران‌های برتر شهر</span>
          </h1>
          <p class="hero-description">
            بهترین غذاها از بهترین رستوران‌ها، همین الان سفارش دهید!
          </p>
          <div class="stats-row">
            <div class="stat-item">
              <span class="stat-number">{{ restaurants.length }}+</span>
              <span class="stat-label">رستوران</span>
            </div>
            <div class="stat-item">
              <span class="stat-number">1000+</span>
              <span class="stat-label">منوی متنوع</span>
            </div>
            <div class="stat-item">
              <span class="stat-number">⚡</span>
              <span class="stat-label">تحویل سریع</span>
            </div>
          </div>
        </div>
        <div class="hero-visual">
          <div class="floating-emoji">🍕</div>
          <div class="floating-emoji">🍔</div>
          <div class="floating-emoji">🍜</div>
          <div class="floating-emoji">🥗</div>
          <div class="floating-emoji">🍰</div>
        </div>
      </div>
    </section>

    <!-- Search & Filter Section -->
    <section class="search-section">
      <div class="search-container">
        <div class="search-box">
          <i class="search-icon">🔍</i>
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="نام رستوران، نوع غذا یا محله را جستجو کنید..."
            class="search-input"
          >
        </div>
        <div class="filter-buttons">
          <button 
            v-for="category in categories" 
            :key="category.id"
            @click="selectedCategory = category.id"
            :class="['filter-btn', { active: selectedCategory === category.id }]"
          >
            <span class="category-icon">{{ category.icon }}</span>
            {{ category.name }}
          </button>
        </div>
      </div>
    </section>

    <!-- Loading State -->
    <div v-if="loading" class="loading-section">
      <div class="loading-container">
        <div class="loading-spinner"></div>
        <div class="loading-text">
          <h3>در حال بارگذاری رستوران‌ها...</h3>
          <p>لطفا کمی صبر کنید 🍽️</p>
        </div>
      </div>
    </div>

    <!-- Error State -->
    <div v-if="error" class="error-section">
      <div class="error-container">
        <div class="error-icon">😞</div>
        <h3>مشکلی پیش آمده!</h3>
        <p>{{ error }}</p>
        <button @click="retryLoading" class="retry-button">
          <i class="retry-icon">🔄</i>
          تلاش مجدد
        </button>
      </div>
    </div>
    
    <!-- Restaurants Grid -->
    <section v-if="filteredRestaurants.length" class="restaurants-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">🏪</span>
          رستوران‌های موجود
          <span class="results-count">({{ filteredRestaurants.length }} رستوران)</span>
        </h2>
      </div>

      <div class="restaurant-grid">
        <RouterLink 
          v-for="restaurant in filteredRestaurants" 
          :key="restaurant.id" 
          :to="`/restaurants/${restaurant.id}`" 
          class="restaurant-card-link"
        >
          <div class="restaurant-card">
            <div class="card-header">
              <div class="restaurant-avatar">
                {{ restaurant.name.charAt(0) }}
              </div>
              <div class="card-badge">
                <span class="badge-icon">⭐</span>
                <span>4.5</span>
              </div>
            </div>
            
            <div class="card-content">
              <h3 class="restaurant-name">{{ restaurant.name }}</h3>
              <div class="restaurant-info">
                <div class="info-item">
                  <i class="info-icon">📍</i>
                  <span>{{ restaurant.address }}</span>
                </div>
                <div class="info-item">
                  <i class="info-icon">📞</i>
                  <span>{{ restaurant.phone_number }}</span>
                </div>
              </div>
            </div>

            <div class="card-footer">
              <div class="delivery-info">
                <span class="delivery-time">
                  <i class="time-icon">⏱️</i>
                  25-35 دقیقه
                </span>
                <span class="delivery-fee">
                  <i class="fee-icon">🚀</i>
                  ارسال رایگان
                </span>
              </div>
              <div class="view-menu-btn">
                مشاهده منو
                <i class="arrow-icon">←</i>
              </div>
            </div>

            <div class="card-overlay"></div>
          </div>
        </RouterLink>
      </div>
    </section>

    <!-- Empty State -->
    <div v-else-if="!loading && !error" class="empty-state">
      <div class="empty-container">
        <div class="empty-icon">🔍</div>
        <h3>رستورانی یافت نشد</h3>
        <p>متأسفانه رستورانی با این مشخصات پیدا نکردیم</p>
        <button @click="clearFilters" class="clear-filters-btn">
          <i class="clear-icon">🔄</i>
          پاک کردن فیلترها
        </button>
      </div>
    </div>

    <!-- Features Section -->
    <section class="features-section">
      <div class="features-container">
        <h2 class="features-title">چرا FoodieHub؟</h2>
        <div class="features-grid">
          <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <h4>تحویل سریع</h4>
            <p>سفارش شما در کمترین زمان درب منزل</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🔒</div>
            <h4>پرداخت امن</h4>
            <p>پرداخت آنلاین کاملا امن و محرمانه</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🎯</div>
            <h4>کیفیت تضمینی</h4>
            <p>تنها با رستوران‌های معتبر همکاری می‌کنیم</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">💎</div>
            <h4>پشتیبانی 24/7</h4>
            <p>همیشه در خدمت شما هستیم</p>
          </div>
        </div>
      </div>
    </section>
  </main> <!-- <<-- تگ بسته نشده در اینجا اضافه شد -->
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted, computed } from 'vue';
import restaurantService from '../services/restaurantService';

const restaurants = ref([]);
const loading = ref(true);
const error = ref(null);
const searchQuery = ref('');
const selectedCategory = ref('all');

const categories = ref([
  { id: 'all', name: 'همه', icon: '🍽️' },
  { id: 'fast-food', name: 'فست فود', icon: '🍔' },
  { id: 'traditional', name: 'سنتی', icon: '🍜' },
  { id: 'pizza', name: 'پیتزا', icon: '🍕' },
  { id: 'dessert', name: 'دسر', icon: '🍰' },
  { id: 'healthy', name: 'سالم', icon: '🥗' }
]);

const filteredRestaurants = computed(() => {
  let filtered = restaurants.value;
  
  // Filter by search query
  if (searchQuery.value) {
    filtered = filtered.filter(restaurant =>
      restaurant.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      restaurant.address.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }
  
  return filtered;
});

const retryLoading = async () => {
  loading.value = true;
  error.value = null;
  await loadRestaurants();
};

const clearFilters = () => {
  searchQuery.value = '';
  selectedCategory.value = 'all';
};

const loadRestaurants = async () => {
  try {
    const response = await restaurantService.getRestaurants();
    restaurants.value = response.data;
  } catch (err) {
    error.value = 'خطا در دریافت اطلاعات رستوران‌ها. لطفا دوباره تلاش کنید.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};

onMounted(loadRestaurants);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap');

.home-view {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  font-family: 'Vazirmatn', sans-serif;
}

/* Hero Section */
.hero-section {
  padding: 80px 20px 60px;
  background: linear-gradient(135deg, #850411 0%, #7d0202 100%);
  color: white;
  position: relative;
  overflow: hidden;
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.main-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  line-height: 1.2;
}

.title-highlight {
  display: block;
  background: linear-gradient(135deg, #fff, #f8f9fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.title-subtitle {
  display: block;
  font-size: 2rem;
  font-weight: 600;
  margin-top: 10px;
  opacity: 0.9;
}

.hero-description {
  font-size: 1.3rem;
  line-height: 1.6;
  margin-bottom: 40px;
  opacity: 0.9;
}

.stats-row {
  display: flex;
  gap: 40px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.8;
}

.hero-visual {
  position: relative;
  height: 400px;
}

.floating-emoji {
  position: absolute;
  font-size: 3rem;
  animation: float 3s ease-in-out infinite;
}

.floating-emoji:nth-child(1) {
  top: 10%;
  left: 20%;
  animation-delay: 0s;
}

.floating-emoji:nth-child(2) {
  top: 30%;
  right: 10%;
  animation-delay: 0.6s;
}

.floating-emoji:nth-child(3) {
  bottom: 30%;
  left: 10%;
  animation-delay: 1.2s;
}

.floating-emoji:nth-child(4) {
  bottom: 10%;
  right: 30%;
  animation-delay: 1.8s;
}

.floating-emoji:nth-child(5) {
  top: 50%;
  left: 50%;
  animation-delay: 2.4s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

/* Search Section */
.search-section {
  padding: 40px 20px;
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.search-container {
  max-width: 1200px;
  margin: 0 auto;
}

.search-box {
  position: relative;
  margin-bottom: 30px;
}

.search-icon {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2rem;
  color: #666;
}

.search-input {
  width: 100%;
  padding: 18px 60px 18px 20px;
  border: 2px solid #e1e5e9;
  border-radius: 50px;
  font-size: 1.1rem;
  font-family: 'Vazirmatn', sans-serif;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.9);
}

.search-input:focus {
  outline: none;
  border-color: #7e0404;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.filter-buttons {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  justify-content: center;
}

.filter-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border: 2px solid #e1e5e9;
  border-radius: 25px;
  background: white;
  color: #666;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn:hover {
  border-color: #740202;
  color: #7b0101;
}

.filter-btn.active {
  background: #790101;
  color: white;
  border-color: #6d0202;
}

.category-icon {
  font-size: 1.2rem;
}

/* Loading Section */
.loading-section {
  padding: 80px 20px;
  text-align: center;
}

.loading-container {
  max-width: 400px;
  margin: 0 auto;
}

.loading-spinner {
  width: 60px;
  height: 60px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #9c0505;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 30px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text h3 {
  color: #333;
  margin-bottom: 10px;
  font-size: 1.5rem;
}

.loading-text p {
  color: #666;
  font-size: 1.1rem;
}

/* Error Section */
.error-section {
  padding: 80px 20px;
  text-align: center;
}

.error-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 40px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.error-icon {
  font-size: 4rem;
  margin-bottom: 20px;
}

.error-container h3 {
  color: #e74c3c;
  margin-bottom: 15px;
  font-size: 1.5rem;
}

.error-container p {
  color: #666;
  margin-bottom: 30px;
  line-height: 1.6;
}

.retry-button {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 15px 30px;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.retry-button:hover {
  background: #c0392b;
  transform: translateY(-2px);
}

/* Restaurants Section */
.restaurants-section {
  padding: 60px 20px;
  max-width: 1400px;
  margin: 0 auto;
}

.section-header {
  margin-bottom: 40px;
  text-align: center;
}

.section-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  margin-bottom: 10px;
}

.title-icon {
  font-size: 2.5rem;
}

.results-count {
  font-size: 1.2rem;
  color: #666;
  font-weight: 500;
}

.restaurant-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
}

.restaurant-card-link {
  text-decoration: none;
  color: inherit;
}

.restaurant-card {
  background: white;
  border-radius: 20px;
  padding: 25px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.restaurant-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.restaurant-avatar {
  width: 60px;
  height: 60px;
  border-radius: 15px;
  background: linear-gradient(135deg, #7c0204, #6c0303);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 700;
}

.card-badge {
  display: flex;
  align-items: center;
  gap: 5px;
  background: #f8f9fa;
  padding: 8px 12px;
  border-radius: 20px;
  font-weight: 600;
  color: #333;
}

.badge-icon {
  color: #ffd700;
}

.card-content {
  margin-bottom: 25px;
}

.restaurant-name {
  font-size: 1.4rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 15px;
}

.restaurant-info {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #666;
  font-size: 0.95rem;
}

.info-icon {
  font-size: 1.1rem;
  width: 20px;
  text-align: center;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 20px;
  border-top: 1px solid #f0f0f0;
}

.delivery-info {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.delivery-time,
.delivery-fee {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.9rem;
  color: #666;
}

.view-menu-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: linear-gradient(135deg, #9a0303, #9f0505);
  color: white;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.restaurant-card:hover .view-menu-btn {
  background: linear-gradient(135deg, #900303, #880005);
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.restaurant-card:hover .card-overlay {
  opacity: 1;
}

/* Empty State */
.empty-state {
  padding: 80px 20px;
  text-align: center;
}

.empty-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 60px 40px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.empty-icon {
  font-size: 5rem;
  margin-bottom: 25px;
}

.empty-container h3 {
  color: #333;
  margin-bottom: 15px;
  font-size: 1.5rem;
}

.empty-container p {
  color: #666;
  margin-bottom: 30px;
  line-height: 1.6;
}

.clear-filters-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 15px 30px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.clear-filters-btn:hover {
  background: #5a67d8;
  transform: translateY(-2px);
}

/* Features Section */
.features-section {
  padding: 80px 20px;
  background: white;
}

.features-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.features-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 50px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
}

.feature-item {
  padding: 30px 20px;
  border-radius: 15px;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
  transition: all 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 20px;
}

.feature-item h4 {
  font-size: 1.3rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 15px;
}

.feature-item p {
  color: #666;
  line-height: 1.6;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 40px;
  }
  
  .main-title {
    font-size: 2.5rem;
  }
  
  .title-subtitle {
    font-size: 1.5rem;
  }
  
  .stats-row {
    justify-content: center;
    gap: 30px;
  }
  
  .restaurant-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .filter-buttons {
    justify-content: flex-start;
    overflow-x: auto;
    padding-bottom: 10px;
  }
  
  .filter-btn {
    flex-shrink: 0;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}

@media (max-width: 480px) {
  .hero-section {
    padding: 60px 15px 40px;
  }
  
  .main-title {
    font-size: 2rem;
  }
  
  .search-section {
    padding: 30px 15px;
  }
  
  .restaurant-card {
    padding: 20px;
  }
  
  .card-footer {
    flex-direction: column;
    gap: 15px;
    align-items: stretch;
  }
  
  .view-menu-btn {
    justify-content: center;
  }
}
</style>