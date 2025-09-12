<template>
  <div class="restaurant-detail-page">
    <!-- Loading State -->
    <div v-if="loading" class="loading-section">
      <div class="loading-container">
        <div class="loading-spinner"></div>
        <div class="loading-content">
          <h3>در حال بارگذاری جزئیات رستوران...</h3>
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
    
    <!-- Main Restaurant Detail -->
    <div v-if="restaurant" class="restaurant-detail">
      <!-- Restaurant Header -->
      <header class="restaurant-header">
        <div class="header-background">
          <div class="header-overlay"></div>
          <div class="header-pattern"></div>
        </div>
        
        <div class="header-content">
          <div class="restaurant-avatar">
            {{ restaurant.name.charAt(0) }}
          </div>
          
          <div class="restaurant-info">
            <h1 class="restaurant-name">{{ restaurant.name }}</h1>
            <div class="restaurant-details">
              <div class="detail-item">
                <i class="detail-icon">📍</i>
                <span>{{ restaurant.address }}</span>
              </div>
              <div class="detail-item">
                <i class="detail-icon">📞</i>
                <span>{{ restaurant.phone_number }}</span>
              </div>
            </div>
            
            <div class="restaurant-badges">
              <div class="badge">
                <span class="badge-icon">⭐</span>
                <span>4.5</span>
              </div>
              <div class="badge">
                <span class="badge-icon">⏱️</span>
                <span>25-35 دقیقه</span>
              </div>
              <div class="badge">
                <span class="badge-icon">🚀</span>
                <span>ارسال رایگان</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- Menu Section -->
      <section class="menu-section">
        <div class="section-header">
          <h2 class="section-title">
            <span class="title-icon">🍽️</span>
            منوی غذا
            <span v-if="restaurant.food_items && restaurant.food_items.length" class="menu-count">
              ({{ restaurant.food_items.length }} آیتم)
            </span>
          </h2>
        </div>
        
        <!-- Menu Items -->
        <div v-if="restaurant.food_items && restaurant.food_items.length > 0" class="menu-grid">
          <div 
            v-for="item in restaurant.food_items" 
            :key="item.id" 
            class="menu-item"
            :class="{ 'unavailable': !item.is_available }"
          >
            <!-- Food Image -->
            <div class="item-image-container">
              <img 
                v-if="item.image" 
                :src="getFullImageUrl(item.image)" 
                :alt="item.name" 
                class="food-image"
                @error="handleImageError"
              >
              <div v-else class="no-image">
                <span class="no-image-icon">🍽️</span>
              </div>
              
              <div v-if="!item.is_available" class="unavailable-overlay">
                <span class="unavailable-text">ناموجود</span>
              </div>
              
              <div class="image-gradient"></div>
            </div>
            
            <!-- Item Content -->
            <div class="item-content">
              <div class="item-header">
                <h3 class="item-name">{{ item.name }}</h3>
                <div class="item-rating">
                  <span class="rating-stars">⭐⭐⭐⭐⭐</span>
                  <span class="rating-count">(24)</span>
                </div>
              </div>
              
              <p v-if="item.description" class="item-description">
                {{ item.description }}
              </p>
              <p v-else class="item-description placeholder">
                توضیحاتی برای این غذا ثبت نشده است.
              </p>
            </div>
            
            <!-- Item Footer -->
            <div class="item-footer">
              <div class="price-section">
                <span class="price">{{ formatPrice(item.price) }}</span>
                <span class="currency">تومان</span>
              </div>
              
              <div class="add-to-cart-section">
                <div v-if="getItemQuantity(item.id) > 0" class="quantity-controls">
                  <button 
                    @click="removeFromCart(item)" 
                    class="quantity-btn minus"
                  >
                    −
                  </button>
                  <span class="quantity">{{ getItemQuantity(item.id) }}</span>
                  <button 
                    @click="addToCart(item)" 
                    class="quantity-btn plus"
                    :disabled="!item.is_available"
                  >
                    +
                  </button>
                </div>
                
                <button 
                  v-else
                  @click="addToCart(item)" 
                  :disabled="!item.is_available"
                  class="add-to-cart-btn"
                >
                  <span v-if="item.is_available" class="btn-content">
                    <i class="cart-icon">🛒</i>
                    افزودن به سبد
                  </span>
                  <span v-else class="btn-content unavailable">
                    <i class="unavailable-icon">❌</i>
                    ناموجود
                  </span>
                </button>
              </div>
            </div>

            <div class="item-overlay"></div>
          </div>
        </div>
        
        <!-- Empty Menu State -->
        <div v-else class="empty-menu">
          <div class="empty-container">
            <div class="empty-icon">🍽️</div>
            <h3>منویی موجود نیست</h3>
            <p>این رستوران در حال حاضر منویی ثبت نکرده است.</p>
            <p class="empty-subtitle">لطفا بعداً مراجعه کنید یا با رستوران تماس بگیرید.</p>
          </div>
        </div>
      </section>

      <!-- Cart Summary (if items in cart) -->
      <div v-if="cartStore.items.length > 0" class="cart-summary">
        <div class="cart-info">
          <span class="cart-items">{{ cartStore.items.length }} آیتم</span>
          <span class="cart-total">{{ formatPrice(cartStore.total) }} تومان</span>
        </div>
        <button class="view-cart-btn" @click="goToCart">
          <span class="cart-icon">🛒</span>
          مشاهده سبد خرید
          <i class="arrow-icon">←</i>
        </button>
      </div>
    </div>
  </div> <!-- <<-- تگ بسته نشده در اینجا اضافه شد -->
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import restaurantService from '../services/restaurantService';
import { useCartStore } from '../stores/cartStore';

const route = useRoute();
const router = useRouter();
const cartStore = useCartStore();

const restaurant = ref(null);
const loading = ref(true);
const error = ref(null);

const getFullImageUrl = (imagePath) => {
  if (!imagePath) return '';
  
  if (imagePath.startsWith('http')) {
    return imagePath;
  }
  
  return `http://127.0.0.1:8000${imagePath}`;
};

const formatPrice = (price) => {
  return parseFloat(price).toLocaleString('fa-IR');
};

const handleImageError = (event) => {
  event.target.style.display = 'none';
  event.target.nextElementSibling.style.display = 'flex';
};

const getItemQuantity = (itemId) => {
  const cartItem = cartStore.items.find(item => item.id === itemId);
  return cartItem ? cartItem.quantity : 0;
};

const addToCart = (foodItem) => {
  cartStore.addItem(foodItem);
};

const removeFromCart = (foodItem) => {
  cartStore.removeItem(foodItem.id);
};

const goToCart = () => {
  router.push('/cart');
};

const loadRestaurant = async () => {
  const restaurantId = route.params.id;
  
  try {
    const response = await restaurantService.getRestaurantDetail(restaurantId);
    restaurant.value = response.data;
  } catch (err) {
    error.value = 'خطا در دریافت جزئیات رستوران. لطفاً دوباره تلاش کنید.';
    console.error("Failed to fetch restaurant details:", err);
  } finally {
    loading.value = false;
  }
};

const retryLoading = async () => {
  loading.value = true;
  error.value = null;
  await loadRestaurant();
};

onMounted(loadRestaurant);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap');

.restaurant-detail-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  font-family: 'Vazirmatn', sans-serif;
}

/* Loading State */
.loading-section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}

.loading-container {
  text-align: center;
  background: white;
  padding: 50px 40px;
  border-radius: 20px;
  box-shadow: 0 15px 40px rgba(220, 20, 60, 0.1);
  border: 2px solid #dc143c;
}

.loading-spinner {
  width: 60px;
  height: 60px;
  border: 4px solid #f8f9fa;
  border-top: 4px solid #dc143c;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 30px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-content h3 {
  color: #212529;
  margin-bottom: 10px;
  font-size: 1.5rem;
  font-weight: 700;
}

.loading-content p {
  color: #666;
  font-size: 1.1rem;
}

/* Error State */
.error-section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}

.error-container {
  text-align: center;
  background: white;
  padding: 50px 40px;
  border-radius: 20px;
  box-shadow: 0 15px 40px rgba(220, 20, 60, 0.1);
  border: 2px solid #dc143c;
  max-width: 500px;
}

.error-icon {
  font-size: 4rem;
  margin-bottom: 20px;
}

.error-container h3 {
  color: #dc143c;
  margin-bottom: 15px;
  font-size: 1.5rem;
  font-weight: 700;
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
  background: #dc143c;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(220, 20, 60, 0.3);
}

.retry-button:hover {
  background: #b91c3c;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.4);
}

/* Restaurant Detail */
.restaurant-detail {
  max-width: 1200px;
  margin: 0 auto;
  background: white;
  min-height: 100vh;
  position: relative;
}

/* Restaurant Header */
.restaurant-header {
  position: relative;
  background: linear-gradient(135deg, #dc143c 0%, #b91c3c 100%);
  color: white;
  overflow: hidden;
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.header-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(220, 20, 60, 0.9), rgba(185, 28, 60, 0.9));
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
    transparent 10px,
    rgba(255, 255, 255, 0.05) 10px,
    rgba(255, 255, 255, 0.05) 20px
  );
}

.header-content {
  position: relative;
  z-index: 2;
  padding: 60px 40px;
  display: flex;
  align-items: center;
  gap: 40px;
}

.restaurant-avatar {
  width: 120px;
  height: 120px;
  border-radius: 20px;
  background: white;
  color: #dc143c;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 800;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  border: 4px solid rgba(255, 255, 255, 0.2);
}

.restaurant-info {
  flex: 1;
}

.restaurant-name {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 20px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.restaurant-details {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 30px;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 15px;
  font-size: 1.2rem;
}

.detail-icon {
  font-size: 1.5rem;
  width: 30px;
  text-align: center;
}

.restaurant-badges {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: 12px 20px;
  border-radius: 25px;
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.badge-icon {
  font-size: 1.2rem;
}

/* Menu Section */
.menu-section {
  padding: 60px 40px;
}

.section-header {
  text-align: center;
  margin-bottom: 50px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #212529;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  margin-bottom: 10px;
}

.title-icon {
  font-size: 3rem;
}

.menu-count {
  font-size: 1.2rem;
  color: #dc143c;
  font-weight: 600;
}

/* Menu Grid */
.menu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
}

.menu-item {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.1);
  transition: all 0.3s ease;
  position: relative;
  border: 2px solid transparent;
}

.menu-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 40px rgba(220, 20, 60, 0.2);
  border-color: #dc143c;
}

.menu-item.unavailable {
  opacity: 0.7;
  filter: grayscale(0.5);
}

.item-image-container {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.food-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.menu-item:hover .food-image {
  transform: scale(1.1);
}

.no-image {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #dc143c;
}

.no-image-icon {
  font-size: 4rem;
}

.unavailable-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: 700;
}

.image-gradient {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.3));
}

.item-content {
  padding: 25px;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 15px;
}

.item-name {
  font-size: 1.4rem;
  font-weight: 700;
  color: #212529;
  margin: 0;
}

.item-rating {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 5px;
}

.rating-stars {
  color: #ffd700;
  font-size: 0.9rem;
}

.rating-count {
  color: #666;
  font-size: 0.8rem;
}

.item-description {
  color: #666;
  line-height: 1.6;
  margin: 0;
  font-size: 0.95rem;
}

.item-description.placeholder {
  font-style: italic;
  opacity: 0.7;
}

.item-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 25px;
  border-top: 1px solid #f0f0f0;
  background: #fafafa;
}

.price-section {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.price {
  font-size: 1.5rem;
  font-weight: 800;
  color: #dc143c;
}

.currency {
  font-size: 1rem;
  color: #666;
  font-weight: 500;
}

.add-to-cart-section {
  display: flex;
  align-items: center;
}

.quantity-controls {
  display: flex;
  align-items: center;
  gap: 15px;
  background: white;
  border: 2px solid #dc143c;
  border-radius: 10px;
  padding: 5px;
}

.quantity-btn {
  width: 35px;
  height: 35px;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.quantity-btn.minus {
  background: #f8f9fa;
  color: #dc143c;
}

.quantity-btn.plus {
  background: #dc143c;
  color: white;
}

.quantity-btn:hover {
  transform: scale(1.1);
}

.quantity-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.quantity {
  font-size: 1.2rem;
  font-weight: 700;
  color: #212529;
  min-width: 30px;
  text-align: center;
}

.add-to-cart-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 25px;
  background: #dc143c;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(220, 20, 60, 0.3);
}

.add-to-cart-btn:hover:not(:disabled) {
  background: #b91c3c;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.4);
}

.add-to-cart-btn:disabled {
  background: #666;
  cursor: not-allowed;
  box-shadow: none;
}

.btn-content.unavailable {
  color: #ccc;
}

.cart-icon {
  font-size: 1.2rem;
}

.item-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(220, 20, 60, 0.05), rgba(185, 28, 60, 0.05));
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}

.menu-item:hover .item-overlay {
  opacity: 1;
}

/* Empty Menu */
.empty-menu {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 400px;
}

.empty-container {
  text-align: center;
  background: white;
  padding: 60px 40px;
  border-radius: 20px;
  box-shadow: 0 15px 40px rgba(220, 20, 60, 0.1);
  border: 2px solid #dc143c;
  max-width: 500px;
}

.empty-icon {
  font-size: 5rem;
  margin-bottom: 25px;
  color: #dc143c;
}

.empty-container h3 {
  color: #212529;
  margin-bottom: 15px;
  font-size: 1.5rem;
  font-weight: 700;
}

.empty-container p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 10px;
}

.empty-subtitle {
  font-size: 0.9rem;
  font-style: italic;
}

/* Cart Summary */
.cart-summary {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: #dc143c;
  color: white;
  padding: 20px 30px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  box-shadow: 0 10px 30px rgba(220, 20, 60, 0.3);
  z-index: 1000;
  min-width: 350px;
}

.cart-info {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.cart-items {
  font-size: 0.9rem;
  opacity: 0.9;
}

.cart-total {
  font-size: 1.2rem;
  font-weight: 700;
}

.view-cart-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 20px;
  background: white;
  color: #dc143c;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-cart-btn:hover {
  background: #f8f9fa;
  transform: translateY(-2px);
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
    padding: 40px 20px;
  }
  
  .restaurant-name {
    font-size: 2rem;
  }
  
  .restaurant-badges {
    justify-content: center;
  }
  
  .menu-section {
    padding: 40px 20px;
  }
  
  .menu-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .section-title {
    font-size: 2rem;
    flex-direction: column;
    gap: 10px;
  }
  
  .cart-summary {
    left: 20px;
    right: 20px;
    transform: none;
    min-width: auto;
  }
}

@media (max-width: 480px) {
  .restaurant-avatar {
    width: 80px;
    height: 80px;
    font-size: 2rem;
  }
  
  .item-footer {
    flex-direction: column;
    gap: 20px;
    align-items: stretch;
  }
  
  .add-to-cart-btn,
  .quantity-controls {
    width: 100%;
    justify-content: center;
  }
  
  .cart-summary {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }
}
</style>