<!-- src/views/OrderHistoryView.vue -->
<template>
  <div class="history-page">
    <div class="history-container">
      <h1 class="history-title">📋 تاریخچه سفارشات</h1>

      <div v-if="loading" class="loading-box">
        <div class="spinner"></div>
        <p>در حال بارگذاری...</p>
      </div>

      <div v-else-if="orders.length === 0" class="empty-box">
        <p>شما تاکنون سفارشی ثبت نکرده‌اید.</p>
      </div>

      <div v-else class="order-list">
        <div v-for="order in orders" :key="order.id" class="order-card">
          <div class="order-header">
            <h3>🍽️ {{ order.restaurant_name }}</h3>
            <span class="status-badge" :class="getStatusClass(order.status)">
              {{ getStatusText(order.status) }}
            </span>
          </div>
          <div class="order-info">
            <p><strong>📅 تاریخ:</strong> {{ new Date(order.created_at).toLocaleDateString('fa-IR') }}</p>
            <p><strong>💰 مبلغ کل:</strong> {{ formatPrice(order.total_price) }} تومان</p>
          </div>
          <ul class="order-items">
            <li v-for="item in order.items" :key="item.food_name">
              <span>{{ item.quantity }} ×</span> {{ item.food_name }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import orderService from "../services/orderService";

const orders = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const response = await orderService.getMyOrders();
    orders.value = response.data;
  } catch (error) {
    console.error("Failed to fetch order history:", error);
  } finally {
    loading.value = false;
  }
});

const formatPrice = (price) => parseFloat(price).toLocaleString("fa-IR");

const getStatusText = (status) => {
  switch (status) {
    case "pending":
      return "در حال پردازش";
    case "completed":
      return "تکمیل شده";
    case "cancelled":
      return "لغو شده";
    default:
      return status;
  }
};

const getStatusClass = (status) => {
  switch (status) {
    case "pending":
      return "pending";
    case "completed":
      return "completed";
    case "cancelled":
      return "cancelled";
    default:
      return "default";
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;800&display=swap");

.history-page {
  min-height: 100vh;
  background: #fff; /* پس‌زمینه سفید */
  color: #000; /* نوشته‌ها مشکی */
  font-family: "Vazirmatn", sans-serif;
  display: flex;
  justify-content: center;
  padding: 50px 20px;
}

.history-container {
  width: 100%;
  max-width: 1200px; /* عرض صفحه بزرگ‌تر */
}

.history-title {
  font-size: 2.5rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 40px;
  color: #dc143c; /* قرمز پررنگ */
}

/* بارگذاری و خالی */
.loading-box,
.empty-box {
  text-align: center;
  border: 2px solid #dc143c;
  border-radius: 15px;
  padding: 40px;
  font-size: 1.2rem;
  font-weight: 600;
}

/* لیست سفارشات → دو به دو */
.order-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 25px;
}

/* کارت سفارش */
.order-card {
  border: 3px solid #dc143c; /* دور کادر قرمز */
  border-radius: 20px;
  padding: 30px;
  background: #fff;
  color: #000;
  font-size: 1.1rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.order-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(220, 20, 60, 0.2);
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.order-header h3 {
  font-size: 1.6rem;
  font-weight: 700;
}

/* وضعیت سفارش */
.status-badge {
  padding: 6px 14px;
  border-radius: 15px;
  font-size: 1rem;
  font-weight: 600;
  border: 2px solid #dc143c;
}
.status-badge.pending {
  background: #fff3e0;
  color: #e65100;
}
.status-badge.completed {
  background: #e8f5e9;
  color: #2e7d32;
}
.status-badge.cancelled {
  background: #ffebee;
  color: #b71c1c;
}
.status-badge.default {
  background: #f5f5f5;
  color: #444;
}

/* اطلاعات سفارش */
.order-info p {
  margin: 10px 0;
  font-size: 1rem;
}
.order-info strong {
  color: #000;
}

/* آیتم‌ها */
.order-items {
  margin-top: 20px;
  padding-right: 25px;
  list-style: none;
}
.order-items li {
  margin: 8px 0;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: #fafafa;
}

/* ریسپانسیو */
@media (max-width: 768px) {
  .order-list {
    grid-template-columns: 1fr; /* تک‌ستونه در موبایل */
  }
  .order-card {
    padding: 20px;
    font-size: 1rem;
  }
  .order-header {
    flex-direction: column;
    gap: 10px;
  }
}
</style>
