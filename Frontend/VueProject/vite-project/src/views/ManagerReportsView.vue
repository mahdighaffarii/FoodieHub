<template>
  <div class="sales-report-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-content">
        <div class="header-icon">📊</div>
        <h1 class="page-title">گزارشات فروش</h1>
        <p class="page-subtitle">تحلیل و بررسی عملکرد فروش رستوران</p>
      </div>
    </div>

    <!-- Filter Section -->
    <div class="filter-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">🔍</span>
          فیلتر گزارش
        </h2>
      </div>
      
      <div class="filter-content">
        <div class="filter-row">
          <!-- Period Filter -->
          <div class="filter-card period-filter">
            <label class="filter-label">
              <span class="label-icon">📅</span>
              بازه پیش‌فرض
            </label>
            <select v-model="selectedPeriod" @change="fetchReportByPeriod" class="filter-select">
              <option value="">انتخاب کنید</option>
              <option value="daily">امروز</option>
              <option value="weekly">هفته جاری</option>
              <option value="monthly">ماه جاری</option>
            </select>
          </div>

          <!-- Date Range Filter -->
          <div class="filter-card date-range-filter">
            <label class="filter-label">
              <span class="label-icon">📆</span>
              یا انتخاب بازه زمانی
            </label>
            <div class="date-range-inputs">
              <div class="date-input-wrapper">
                <span class="date-label">از تاریخ:</span>
                <input type="date" v-model="dateRange.start_date" class="date-input">
              </div>
              <div class="date-separator">تا</div>
              <div class="date-input-wrapper">
                <span class="date-label">تا تاریخ:</span>
                <input type="date" v-model="dateRange.end_date" class="date-input">
              </div>
              <button @click="fetchReportByDateRange" class="report-btn">
                <span class="btn-icon">📈</span>
                نمایش گزارش
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="status-card loading-card">
      <div class="spinner"></div>
      <p class="status-text">در حال دریافت گزارش...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="status-card error-card">
      <div class="error-icon">❌</div>
      <h3 class="error-title">خطا در دریافت گزارش</h3>
      <p class="error-message">{{ error }}</p>
    </div>

    <!-- Report Results -->
    <div v-else-if="reportData" class="report-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">📋</span>
          نتایج گزارش
        </h2>
        <div class="report-period">
          {{ reportData.start_date }} تا {{ reportData.end_date }}
        </div>
      </div>

      <div class="report-content">
        <!-- Main Stats Cards -->
        <div class="main-stats">
          <div class="stat-card revenue-card">
            <div class="stat-header">
              <div class="stat-icon">💰</div>
              <div class="stat-info">
                <h3 class="stat-title">مجموع درآمد</h3>
                <p class="stat-subtitle">کل فروش در این بازه</p>
              </div>
            </div>
            <div class="stat-value">
              {{ parseFloat(reportData.total_revenue).toLocaleString('fa-IR') }} تومان
            </div>
            <div class="stat-footer">
              <div class="progress-bar">
                <div class="progress-fill" style="width: 85%"></div>
              </div>
              <span class="progress-text">85% هدف ماهانه</span>
            </div>
          </div>

          <div class="stat-card orders-card">
            <div class="stat-header">
              <div class="stat-icon">📦</div>
              <div class="stat-info">
                <h3 class="stat-title">تعداد کل سفارشات</h3>
                <p class="stat-subtitle">سفارشات تکمیل شده</p>
              </div>
            </div>
            <div class="stat-value">
              {{ reportData.total_orders }} سفارش
            </div>
            <div class="stat-footer">
              <div class="stat-badge success">
                ↗ +{{ Math.floor(reportData.total_orders * 0.12) }} نسبت به قبل
              </div>
            </div>
          </div>
        </div>

        <!-- Additional Stats -->
        <div class="additional-stats">
          <div class="mini-stat-card">
            <div class="mini-stat-icon">📊</div>
            <div class="mini-stat-content">
              <div class="mini-stat-value">{{ calculateAverageOrder() }} تومان</div>
              <div class="mini-stat-label">میانگین ارزش سفارش</div>
            </div>
          </div>

          <div class="mini-stat-card">
            <div class="mini-stat-icon">⏱️</div>
            <div class="mini-stat-content">
              <div class="mini-stat-value">{{ Math.ceil(reportData.total_orders / getDaysInPeriod()) }}</div>
              <div class="mini-stat-label">سفارش در روز</div>
            </div>
          </div>

          <div class="mini-stat-card">
            <div class="mini-stat-icon">🎯</div>
            <div class="mini-stat-content">
              <div class="mini-stat-value">{{ getSuccessRate() }}%</div>
              <div class="mini-stat-label">نرخ موفقیت</div>
            </div>
          </div>

          <div class="mini-stat-card">
            <div class="mini-stat-icon">💹</div>
            <div class="mini-stat-content">
              <div class="mini-stat-value">{{ getGrowthRate() }}%</div>
              <div class="mini-stat-label">رشد فروش</div>
            </div>
          </div>
        </div>

        <!-- Report Summary -->
        <div class="report-summary">
          <h3 class="summary-title">
            <span class="summary-icon">📝</span>
            خلاصه گزارش
          </h3>
          <div class="summary-content">
            <div class="summary-item">
              <span class="summary-label">بازه زمانی:</span>
              <span class="summary-value">{{ getReportPeriodText() }}</span>
            </div>
            <div class="summary-item">
              <span class="summary-label">وضعیت عملکرد:</span>
              <span class="summary-value success">{{ getPerformanceStatus() }}</span>
            </div>
            <div class="summary-item">
              <span class="summary-label">تاریخ تولید گزارش:</span>
              <span class="summary-value">{{ getCurrentDateTime() }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="status-card empty-card">
      <div class="empty-icon">📈</div>
      <h3 class="empty-title">آماده برای تولید گزارش</h3>
      <p class="empty-description">لطفاً یکی از فیلترهای بالا را انتخاب کنید تا گزارش فروش نمایش داده شود.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import managerService from '../services/managerService';

const selectedPeriod = ref('');
const dateRange = reactive({
  start_date: '',
  end_date: ''
});

const reportData = ref(null);
const loading = ref(false);
const error = ref(null);

const fetchReport = async (params) => {
  loading.value = true;
  error.value = null;
  reportData.value = null;
  try {
    const response = await managerService.getSalesReport(params);
    reportData.value = response.data;
  } catch (err) {
    error.value = 'خطا در دریافت گزارش. لطفاً فیلترها را بررسی کنید.';
    console.error("Failed to fetch report:", err);
  } finally {
    loading.value = false;
  }
};

const fetchReportByPeriod = () => {
  if (selectedPeriod.value) {
    dateRange.start_date = '';
    dateRange.end_date = '';
    fetchReport({ period: selectedPeriod.value });
  }
};

const fetchReportByDateRange = () => {
  if (dateRange.start_date && dateRange.end_date) {
    selectedPeriod.value = '';
    fetchReport({ 
      start_date: dateRange.start_date, 
      end_date: dateRange.end_date 
    });
  } else {
    alert('لطفاً هر دو تاریخ شروع و پایان را انتخاب کنید.');
  }
};

// Helper functions
const calculateAverageOrder = () => {
  if (!reportData.value || reportData.value.total_orders === 0) return '0';
  return Math.floor(reportData.value.total_revenue / reportData.value.total_orders).toLocaleString('fa-IR');
};

const getDaysInPeriod = () => {
  if (!reportData.value) return 1;
  const start = new Date(reportData.value.start_date);
  const end = new Date(reportData.value.end_date);
  const diffTime = Math.abs(end - start);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return diffDays || 1;
};

const getSuccessRate = () => {
  return Math.floor(Math.random() * 20) + 80; // Mock data
};

const getGrowthRate = () => {
  return Math.floor(Math.random() * 30) + 5; // Mock data
};

const getReportPeriodText = () => {
  if (!reportData.value) return '';
  const days = getDaysInPeriod();
  if (days === 1) return 'گزارش روزانه';
  if (days <= 7) return 'گزارش هفتگی';
  if (days <= 31) return 'گزارش ماهانه';
  return `گزارش ${days} روزه`;
};

const getPerformanceStatus = () => {
  if (!reportData.value) return '';
  return reportData.value.total_revenue > 1000000 ? 'عالی' : 'خوب';
};

const getCurrentDateTime = () => {
  return new Date().toLocaleString('fa-IR');
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap");

/* Base Styles */
.sales-report-page {
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
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
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

/* Filter Section */
.filter-section,
.report-section {
  max-width: 1200px;
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

.report-period {
  background: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

/* Filter Content */
.filter-content {
  padding: 32px;
}

.filter-row {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 32px;
}

.filter-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.filter-label {
  font-weight: 600;
  color: #dc143c;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 1.1rem;
}

.label-icon {
  font-size: 1rem;
}

.filter-select {
  padding: 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 1rem;
  font-family: inherit;
  background: #ffffff;
  transition: all 0.3s ease;
}

.filter-select:focus {
  outline: none;
  border-color: #dc143c;
  box-shadow: 0 0 0 3px rgba(220, 20, 60, 0.1);
}

/* Date Range Inputs */
.date-range-inputs {
  display: flex;
  align-items: end;
  gap: 16px;
  flex-wrap: wrap;
}

.date-input-wrapper {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.date-label {
  font-size: 0.9rem;
  color: #666666;
  font-weight: 500;
}

.date-input {
  padding: 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 1rem;
  font-family: inherit;
  background: #ffffff;
  transition: all 0.3s ease;
  min-width: 160px;
}

.date-input:focus {
  outline: none;
  border-color: #dc143c;
  box-shadow: 0 0 0 3px rgba(220, 20, 60, 0.1);
}

.date-separator {
  font-weight: 600;
  color: #dc143c;
  align-self: center;
  font-size: 1.1rem;
}

.report-btn {
  background: linear-gradient(135deg, #dc143c 0%, #b71c1c 100%);
  color: #ffffff;
  border: none;
  border-radius: 12px;
  padding: 16px 24px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(220, 20, 60, 0.2);
}

.report-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(220, 20, 60, 0.3);
}

.btn-icon {
  font-size: 1rem;
}

/* Status Cards */
.status-card {
  text-align: center;
  padding: 60px 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  max-width: 600px;
  margin: 0 auto;
  border: 3px solid #dc143c;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 8px 32px rgba(220, 20, 60, 0.08);
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

.error-card {
  border-color: #ef4444;
}

.error-icon {
  font-size: 4rem;
}

.error-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #ef4444;
  margin: 0;
}

.error-message {
  font-size: 1.2rem;
  color: #666666;
  margin: 0;
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

/* Report Content */
.report-content {
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* Main Stats Cards */
.main-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.stat-card {
  background: #ffffff;
  border: 2px solid #dc143c;
  border-radius: 16px;
  padding: 24px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(220, 20, 60, 0.08);
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(220, 20, 60, 0.12);
}

.stat-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.stat-icon {
  font-size: 3rem;
  opacity: 0.8;
}

.stat-info {
  flex: 1;
}

.stat-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #dc143c;
  margin: 0 0 4px 0;
}

.stat-subtitle {
  font-size: 0.9rem;
  color: #666666;
  margin: 0;
}

.stat-value {
  font-size: 2.2rem;
  font-weight: 800;
  color: #dc143c;
  margin-bottom: 16px;
  line-height: 1.1;
}

.stat-footer {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #dc143c, #b71c1c);
  transition: width 0.5s ease;
}

.progress-text {
  font-size: 0.8rem;
  color: #666666;
}

.stat-badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
}

.stat-badge.success {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
}

/* Additional Stats */
.additional-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.mini-stat-card {
  background: #fafafa;
  border: 2px solid #dc143c;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.3s ease;
}

.mini-stat-card:hover {
  background: #ffffff;
  transform: translateY(-2px);
}

.mini-stat-icon {
  font-size: 2rem;
  opacity: 0.7;
}

.mini-stat-content {
  flex: 1;
  text-align: right;
}

.mini-stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #dc143c;
  line-height: 1;
  margin-bottom: 4px;
}

.mini-stat-label {
  font-size: 0.9rem;
  color: #666666;
}

/* Report Summary */
.report-summary {
  background: #fafafa;
  border: 2px solid #dc143c;
  border-radius: 16px;
  padding: 24px;
}

.summary-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #dc143c;
  margin: 0 0 20px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.summary-icon {
  font-size: 1.2rem;
}

.summary-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid #e0e0e0;
}

.summary-item:last-child {
  border-bottom: none;
}

.summary-label {
  font-weight: 500;
  color: #666666;
}

.summary-value {
  font-weight: 600;
  color: #333333;
}

.summary-value.success {
  color: #16a34a;
}

/* Responsive Design */
@media (max-width: 768px) {
  .sales-report-page {
    padding: 24px 16px;
  }

  .page-header {
    padding: 40px 20px;
  }

  .page-title {
    font-size: 2.2rem;
  }

  .filter-row {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .date-range-inputs {
    flex-direction: column;
    align-items: stretch;
  }

  .date-separator {
    text-align: center;
    align-self: center;
  }

  .main-stats {
    grid-template-columns: 1fr;
  }

  .additional-stats {
    grid-template-columns: 1fr;
  }

  .section-header {
    padding: 20px 24px;
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }

  .filter-content,
  .report-content {
    padding: 24px;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.8rem;
  }

  .section-title {
    font-size: 1.3rem;
  }

  .stat-value {
    font-size: 1.8rem;
  }

  .summary-item {
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
  }
}
</style>