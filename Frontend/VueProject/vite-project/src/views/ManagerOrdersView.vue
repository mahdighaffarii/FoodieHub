<!-- src/views/ManagerOrdersView.vue -->
<template>
  <div class="manager-orders-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-content">
        <div class="header-icon">📋</div>
        <h1 class="page-title">مدیریت سفارشات</h1>
        <p class="page-subtitle">مشاهده و پردازش سفارشات دریافتی رستوران</p>
      </div>
    </div>

    <!-- Orders Section -->
    <div class="orders-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">🛒</span>
          سفارشات دریافتی
        </h2>
        <div v-if="orders.length > 0" class="orders-count">
          {{ orders.length }} سفارش
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="status-card">
        <div class="spinner"></div>
        <p class="status-text">در حال بارگذاری سفارشات...</p>
      </div>

      <!-- Empty State -->
      <div v-else-if="orders.length === 0" class="status-card empty-state">
        <div class="empty-icon">📦</div>
        <h3 class="empty-title">هیچ سفارشی یافت نشد</h3>
        <p class="empty-description">هنوز هیچ سفارشی برای رستوران شما ثبت نشده است.</p>
      </div>

      <!-- Orders Table -->
      <div v-else class="table-wrapper">
        <table class="orders-table">
          <thead>
            <tr>
              <th>
                <span class="th-content">
                  <span class="th-icon">#️⃣</span>
                  شماره سفارش
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">👤</span>
                  مشتری
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">💰</span>
                  مبلغ کل
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">📅</span>
                  تاریخ ثبت
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">📊</span>
                  وضعیت فعلی
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">⚙️</span>
                  تغییر وضعیت
                </span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in orders" :key="order.id" class="order-row">
              <td class="order-id">
                <span class="id-badge">#{{ order.id }}</span>
              </td>
              <td class="customer-cell">
                <div class="customer-info">
                  <span class="customer-icon">👤</span>
                  <span class="customer-email">{{ order.customer_email || 'نامشخص' }}</span>
                </div>
              </td>
              <td class="price-cell">
                <span class="price-value">{{ order.total_price }} تومان</span>
              </td>
              <td class="date-cell">
                <span class="date-value">{{ new Date(order.created_at).toLocaleString('fa-IR') }}</span>
              </td>
              <td class="status-cell">
                <span :class="['status-badge', getStatusClass(order.status)]">
                  {{ getStatusText(order.status) }}
                </span>
              </td>
              <td class="action-cell">
                <div class="status-selector">
                  <select 
                    :value="order.status"
                    @change="handleStatusChange(order, $event)"
                    class="status-select"
                  >
                    <option value="PENDING">در انتظار</option>
                    <option value="CONFIRMED">تأیید شده</option>
                    <option value="IN_PROGRESS">در حال آماده‌سازی</option>
                    <option value="SENT">ارسال شده</option>
                    <option value="CANCELED">لغو شده</option>
                  </select>
                  <span class="select-arrow">⌄</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Quick Stats -->
    <div class="quick-stats">
      <div class="stat-card">
        <div class="stat-icon">⏳</div>
        <div class="stat-content">
          <div class="stat-number">{{ getPendingOrdersCount() }}</div>
          <div class="stat-label">در انتظار</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🍳</div>
        <div class="stat-content">
          <div class="stat-number">{{ getInProgressOrdersCount() }}</div>
          <div class="stat-label">در حال آماده‌سازی</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">✅</div>
        <div class="stat-content">
          <div class="stat-number">{{ getCompletedOrdersCount() }}</div>
          <div class="stat-label">تکمیل شده</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">💰</div>
        <div class="stat-content">
          <div class="stat-number">{{ getTotalRevenue() }}</div>
          <div class="stat-label">کل درآمد</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import managerService from '../services/managerService';

const orders = ref([]);
const loading = ref(true);

const fetchOrders = async () => {
  try {
    loading.value = true;
    const response = await managerService.getRestaurantOrders();
    orders.value = response.data; 
  } catch (error) {
    console.error("Failed to fetch orders:", error);
    alert('خطا در دریافت سفارشات.');
  } finally {
    loading.value = false;
  }
};

const handleStatusChange = async (order, event) => {
  const newStatus = event.target.value;
  try {
    await managerService.updateOrderStatus(order.id, newStatus);
    await fetchOrders(); 
    alert(`وضعیت سفارش شماره ${order.id} با موفقیت تغییر کرد.`);
  } catch (error) {
    console.error("Failed to update status:", error);
    alert('خطا در تغییر وضعیت سفارش.');
    await fetchOrders();
  }
};

// Helper functions for status
const getStatusClass = (status) => {
  const statusClasses = {
    'PENDING': 'pending',
    'CONFIRMED': 'confirmed',
    'IN_PROGRESS': 'in-progress',
    'SENT': 'sent',
    'CANCELED': 'canceled'
  };
  return statusClasses[status] || 'pending';
};

const getStatusText = (status) => {
  const statusTexts = {
    'PENDING': 'در انتظار',
    'CONFIRMED': 'تأیید شده',
    'IN_PROGRESS': 'در حال آماده‌سازی',
    'SENT': 'ارسال شده',
    'CANCELED': 'لغو شده'
  };
  return statusTexts[status] || status;
};

// Stats calculations
const getPendingOrdersCount = () => {
  return orders.value.filter(order => order.status === 'PENDING').length;
};

const getInProgressOrdersCount = () => {
  return orders.value.filter(order => order.status === 'IN_PROGRESS').length;
};

const getCompletedOrdersCount = () => {
  return orders.value.filter(order => order.status === 'SENT').length;
};

const getTotalRevenue = () => {
  const total = orders.value
    .filter(order => order.status === 'SENT')
    .reduce((sum, order) => sum + parseFloat(order.total_price || 0), 0);
  return total.toLocaleString('fa-IR') + ' تومان';
};

onMounted(fetchOrders);
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap");

/* Base Styles */
.manager-orders-page {
  min-height: 100vh;
  background: #ffffff;
  color: #000000;
  font-family: "Vazirmatn", sans-serif;
  padding: 40px 20px;
  line-height: 1.6;
}

/* Header Section */
.page-header {
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

.page-header::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(220, 20, 60, 0.03) 0%, transparent 70%);
  pointer-events: none;
}

.header-icon {
  font-size: 4rem;
  margin-bottom: 16px;
  display: inline-block;
  animation: bounce 2s ease-in-out infinite;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

.page-title {
  font-size: 3rem;
  font-weight: 800;
  color: #dc143c;
  margin: 0 0 12px 0;
  text-shadow: 0 2px 4px rgba(220, 20, 60, 0.1);
}

.page-subtitle {
  font-size: 1.2rem;
  color: #666666;
  margin: 0;
}

/* Orders Section */
.orders-section {
  max-width: 1400px;
  margin: 0 auto 40px;
  border: 3px solid #dc143c;
  border-radius: 16px;
  background: #ffffff;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(220, 20, 60, 0.08);
}

.section-header {
  background: linear-gradient(135deg, #dc143c 0%, #b71c1c 100%);
  color: #ffffff;
  padding: 24px 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.section-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 12px;
}

.title-icon {
  font-size: 1.5rem;
}

.orders-count {
  background: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

/* Status Cards */
.status-card {
  text-align: center;
  padding: 60px 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f0f0f0;
  border-top: 4px solid #dc143c;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.status-text {
  font-size: 1.3rem;
  font-weight: 500;
  color: #333333;
  margin: 0;
}

.empty-state {
  border-top: 1px solid #f0f0f0;
}

.empty-icon {
  font-size: 4rem;
  opacity: 0.7;
}

.empty-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #dc143c;
  margin: 0;
}

.empty-description {
  font-size: 1.2rem;
  color: #666666;
  margin: 0;
}

/* Table Styles */
.table-wrapper {
  overflow-x: auto;
}

.orders-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 1rem;
}

.orders-table thead tr {
  background: #f8f9fa;
  border-bottom: 2px solid #dc143c;
}

.orders-table th {
  padding: 20px 16px;
  text-align: right;
  font-weight: 700;
  color: #dc143c;
  position: sticky;
  top: 0;
  z-index: 10;
}

.th-content {
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: flex-end;
}

.th-icon {
  font-size: 1.1rem;
}

.order-row {
  transition: all 0.3s ease;
  border-bottom: 1px solid #f0f0f0;
}

.order-row:nth-child(even) {
  background: #fafafa;
}

.order-row:hover {
  background: linear-gradient(90deg, rgba(220, 20, 60, 0.05) 0%, rgba(220, 20, 60, 0.02) 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 20, 60, 0.1);
}

.orders-table td {
  padding: 20px 16px;
  text-align: right;
  vertical-align: middle;
}

/* Cell Specific Styles */
.order-id {
  text-align: center;
}

.id-badge {
  background: rgba(220, 20, 60, 0.1);
  color: #dc143c;
  padding: 6px 12px;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.9rem;
  border: 1px solid rgba(220, 20, 60, 0.2);
}

.customer-info {
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: flex-end;
}

.customer-icon {
  font-size: 1.1rem;
  opacity: 0.7;
}

.customer-email {
  font-weight: 500;
  color: #333333;
}

.price-value {
  font-weight: 700;
  color: #dc143c;
  font-size: 1.1rem;
}

.date-value {
  color: #666666;
  font-size: 0.95rem;
}

/* Status Badges */
.status-badge {
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  border: 1px solid;
  display: inline-block;
}

.status-badge.pending {
  background: rgba(251, 191, 36, 0.1);
  color: #d97706;
  border-color: rgba(251, 191, 36, 0.3);
}

.status-badge.confirmed {
  background: rgba(59, 130, 246, 0.1);
  color: #2563eb;
  border-color: rgba(59, 130, 246, 0.3);
}

.status-badge.in-progress {
  background: rgba(168, 85, 247, 0.1);
  color: #7c3aed;
  border-color: rgba(168, 85, 247, 0.3);
}

.status-badge.sent {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border-color: rgba(34, 197, 94, 0.3);
}

.status-badge.canceled {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
  border-color: rgba(239, 68, 68, 0.3);
}

/* Status Selector */
.status-selector {
  position: relative;
  display: inline-block;
}

.status-select {
  appearance: none;
  background: #ffffff;
  border: 2px solid #dc143c;
  border-radius: 8px;
  padding: 8px 32px 8px 12px;
  font-size: 0.9rem;
  font-weight: 500;
  color: #dc143c;
  cursor: pointer;
  min-width: 140px;
  transition: all 0.3s ease;
}

.status-select:hover {
  background: rgba(220, 20, 60, 0.05);
}

.status-select:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(220, 20, 60, 0.1);
}

.select-arrow {
  position: absolute;
  left: 8px;
  top: 50%;
  transform: translateY(-50%);
  color: #dc143c;
  font-size: 1.2rem;
  pointer-events: none;
}

/* Quick Stats */
.quick-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.stat-card {
  background: #ffffff;
  border: 3px solid #dc143c;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 16px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(220, 20, 60, 0.08);
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(220, 20, 60, 0.12);
}

.stat-icon {
  font-size: 3rem;
  opacity: 0.8;
}

.stat-content {
  flex: 1;
  text-align: right;
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: #dc143c;
  line-height: 1;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 1rem;
  color: #666666;
  font-weight: 500;
}

/* Responsive Design */
@media (max-width: 768px) {
  .manager-orders-page {
    padding: 24px 16px;
  }

  .page-header {
    padding: 40px 20px;
  }

  .page-title {
    font-size: 2.2rem;
  }

  .section-header {
    padding: 20px 24px;
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }

  .section-title {
    font-size: 1.5rem;
  }

  .orders-table th,
  .orders-table td {
    padding: 12px 8px;
    font-size: 0.9rem;
  }

  .customer-info {
    flex-direction: column;
    gap: 4px;
    text-align: center;
  }

  .status-select {
    min-width: 120px;
    font-size: 0.8rem;
  }

  .quick-stats {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
  }

  .stat-card {
    padding: 20px;
    flex-direction: column;
    text-align: center;
  }

  .stat-content {
    text-align: center;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.8rem;
  }

  .section-title {
    font-size: 1.3rem;
  }

  .orders-table {
    font-size: 0.8rem;
  }

  .orders-table th,
  .orders-table td {
    padding: 8px 4px;
  }

  .quick-stats {
    grid-template-columns: 1fr;
  }
}
</style>