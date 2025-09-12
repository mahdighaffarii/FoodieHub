<!-- src/views/WalletHistoryView.vue -->
<template>
  <div class="wallet-page">
    <div class="wallet-container">
      <!-- Header with elegant styling -->
      <div class="header-section">
        <div class="wallet-icon">💰</div>
        <h1 class="wallet-title">تاریخچه کیف پول</h1>
        <p class="subtitle">مشاهده تمامی تراکنش‌های مالی شما</p>
      </div>

      <!-- Loading state with animated spinner -->
      <div v-if="loading" class="status-card loading-card">
        <div class="spinner"></div>
        <p class="status-text">در حال بارگذاری اطلاعات...</p>
      </div>

      <!-- Empty state with icon -->
      <div v-else-if="transactions.length === 0" class="status-card empty-card">
        <div class="empty-icon">📝</div>
        <h3 class="empty-title">هیچ تراکنشی یافت نشد</h3>
        <p class="empty-description">تا کنون هیچ تراکنش مالی ثبت نشده است</p>
      </div>

      <!-- Transactions table with enhanced design -->
      <div v-else class="table-section">
        <div class="table-header">
          <h2 class="section-title">تراکنش‌های اخیر</h2>
          <div class="transaction-count">{{ transactions.length }} تراکنش</div>
        </div>
        
        <div class="table-wrapper">
          <table class="transactions-table">
            <thead>
              <tr>
                <th>
                  <span class="th-content">
                    <span class="th-icon">🏷️</span>
                    نوع تراکنش
                  </span>
                </th>
                <th>
                  <span class="th-content">
                    <span class="th-icon">💵</span>
                    مبلغ (تومان)
                  </span>
                </th>
                <th>
                  <span class="th-content">
                    <span class="th-icon">📋</span>
                    توضیحات
                  </span>
                </th>
                <th>
                  <span class="th-content">
                    <span class="th-icon">📅</span>
                    تاریخ و زمان
                  </span>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="tx in transactions" :key="tx.id" class="transaction-row">
                <td class="transaction-type">
                  <span class="type-badge">{{ tx.transaction_type_display }}</span>
                </td>
                <td class="transaction-amount">
                  <span class="amount-value">{{ formatPrice(tx.amount) }}</span>
                </td>
                <td class="transaction-description">{{ tx.description }}</td>
                <td class="transaction-date">{{ new Date(tx.created_at).toLocaleString('fa-IR') }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import walletService from "../services/walletService";

const transactions = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const response = await walletService.getWalletHistory();
    transactions.value = response.data;
  } catch (error) {
    console.error("Failed to fetch wallet history:", error);
  } finally {
    loading.value = false;
  }
});

const formatPrice = (price) => parseFloat(price).toLocaleString("fa-IR");
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap");

/* Base styles */
.wallet-page {
  min-height: 100vh;
  background: #ffffff;
  color: #000000;
  font-family: "Vazirmatn", sans-serif;
  padding: 40px 20px;
  line-height: 1.6;
}

.wallet-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* Header Section */
.header-section {
  text-align: center;
  padding: 40px 20px;
  border: 3px solid #dc143c;
  border-radius: 20px;
  background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
  box-shadow: 0 8px 32px rgba(220, 20, 60, 0.1);
  position: relative;
  overflow: hidden;
}

.header-section::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(220, 20, 60, 0.03) 0%, transparent 70%);
  pointer-events: none;
}

.wallet-icon {
  font-size: 4rem;
  margin-bottom: 16px;
  display: inline-block;
  animation: bounce 2s infinite;
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

.wallet-title {
  font-size: 3rem;
  font-weight: 800;
  color: #dc143c;
  margin: 0 0 12px 0;
  text-shadow: 0 2px 4px rgba(220, 20, 60, 0.1);
}

.subtitle {
  font-size: 1.2rem;
  font-weight: 400;
  color: #666666;
  margin: 0;
  opacity: 0.8;
}

/* Status Cards */
.status-card {
  text-align: center;
  border: 3px solid #dc143c;
  border-radius: 16px;
  padding: 60px 40px;
  background: #ffffff;
  box-shadow: 0 8px 32px rgba(220, 20, 60, 0.08);
  transition: all 0.3s ease;
}

.loading-card {
  position: relative;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f0f0f0;
  border-top: 4px solid #dc143c;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 24px;
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

.empty-card {
  border-style: dashed;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 20px;
  opacity: 0.7;
}

.empty-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #dc143c;
  margin: 0 0 12px 0;
}

.empty-description {
  font-size: 1.2rem;
  color: #666666;
  margin: 0;
}

/* Table Section */
.table-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 4px;
  flex-wrap: wrap;
  gap: 16px;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: #dc143c;
  margin: 0;
}

.transaction-count {
  background: #dc143c;
  color: #ffffff;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

/* Table Wrapper */
.table-wrapper {
  overflow-x: auto;
  border: 3px solid #dc143c;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 8px 32px rgba(220, 20, 60, 0.08);
}

/* Table Styles */
.transactions-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 1rem;
}

/* Table Header */
.transactions-table thead tr {
  background: linear-gradient(135deg, #dc143c 0%, #b71c1c 100%);
  color: #ffffff;
}

.transactions-table th {
  padding: 20px 24px;
  text-align: right;
  font-weight: 700;
  font-size: 1.1rem;
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
  font-size: 1.2rem;
  opacity: 0.9;
}

/* Table Body */
.transactions-table tbody tr {
  transition: all 0.3s ease;
  border-bottom: 1px solid #f0f0f0;
}

.transactions-table tbody tr:nth-child(even) {
  background: #fafafa;
}

.transactions-table tbody tr:hover {
  background: linear-gradient(90deg, rgba(220, 20, 60, 0.05) 0%, rgba(220, 20, 60, 0.02) 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 20, 60, 0.1);
}

.transactions-table td {
  padding: 20px 24px;
  text-align: right;
  vertical-align: middle;
  font-weight: 500;
}

/* Transaction specific styles */
.transaction-type .type-badge {
  background: rgba(220, 20, 60, 0.1);
  color: #dc143c;
  padding: 6px 12px;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.9rem;
  border: 1px solid rgba(220, 20, 60, 0.2);
}

.transaction-amount .amount-value {
  font-weight: 700;
  font-size: 1.1rem;
  color: #dc143c;
}

.transaction-description {
  color: #555555;
  max-width: 250px;
  word-wrap: break-word;
}

.transaction-date {
  color: #777777;
  font-size: 0.95rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .wallet-page {
    padding: 20px 16px;
  }
  
  .wallet-container {
    gap: 24px;
  }
  
  .header-section {
    padding: 32px 20px;
  }
  
  .wallet-title {
    font-size: 2.2rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .status-card {
    padding: 40px 24px;
  }
  
  .section-title {
    font-size: 1.6rem;
  }
  
  .table-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .transactions-table th,
  .transactions-table td {
    padding: 16px 20px;
    font-size: 0.95rem;
  }
  
  .th-content {
    gap: 6px;
  }
  
  .th-icon {
    font-size: 1rem;
  }
  
  .transaction-description {
    max-width: 200px;
  }
}

@media (max-width: 480px) {
  .wallet-title {
    font-size: 1.8rem;
  }
  
  .transactions-table th,
  .transactions-table td {
    padding: 12px 16px;
    font-size: 0.9rem;
  }
  
  .transaction-description {
    max-width: 150px;
  }
}
</style>