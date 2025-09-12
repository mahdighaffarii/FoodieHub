<template>
  <div class="manager-menu-page">
    <!-- Header Section -->
    <div class="page-header">
      <div class="header-content">
        <div class="header-icon">🍽️</div>
        <h1 class="page-title">مدیریت منو</h1>
        <p class="page-subtitle">افزودن، ویرایش و مدیریت غذاهای رستوران</p>
      </div>
    </div>

    <!-- Add Food Section -->
    <div class="add-food-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">➕</span>
          افزودن غذای جدید
        </h2>
      </div>
      
      <form @submit.prevent="addFoodItem" class="add-food-form">
        <div class="form-row">
          <div class="form-group">
            <label for="name" class="form-label">
              <span class="label-icon">🏷️</span>
              نام غذا
            </label>
            <input 
              type="text" 
              id="name" 
              v-model="newFood.name" 
              required
              class="form-input"
              placeholder="نام غذا را وارد کنید"
            >
          </div>
          
          <div class="form-group">
            <label for="price" class="form-label">
              <span class="label-icon">💰</span>
              قیمت (تومان)
            </label>
            <input 
              type="number" 
              id="price" 
              v-model="newFood.price" 
              required 
              min="0"
              class="form-input"
              placeholder="قیمت به تومان"
            >
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="category" class="form-label">
              <span class="label-icon">📂</span>
              دسته‌بندی
            </label>
            <select id="category" v-model="newFood.category" required class="form-select">
              <option disabled value="">یک دسته‌بندی انتخاب کنید</option>
              <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
            </select>
          </div>
          
          <div class="form-group">
            <label class="form-label">
              <span class="label-icon">✅</span>
              وضعیت
            </label>
            <div class="status-toggle">
              <label class="toggle-label">
                <input type="checkbox" v-model="newFood.is_available" class="toggle-input">
                <span class="toggle-slider"></span>
                <span class="toggle-text">{{ newFood.is_available ? 'موجود' : 'ناموجود' }}</span>
              </label>
            </div>
          </div>
        </div>

        <div class="form-group full-width">
          <label for="description" class="form-label">
            <span class="label-icon">📝</span>
            توضیحات
          </label>
          <textarea 
            id="description" 
            v-model="newFood.description"
            class="form-textarea"
            rows="4"
            placeholder="توضیحات غذا را وارد کنید"
          ></textarea>
        </div>
        
        <button type="submit" class="submit-btn">
          <span class="btn-icon">🍽️</span>
          افزودن غذا به منو
        </button>
      </form>
    </div>
    
    <!-- Menu List Section -->
    <div class="menu-list-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">📋</span>
          منوی فعلی رستوران
        </h2>
        <div v-if="menuItems.length > 0" class="menu-count">
          {{ menuItems.length }} غذا
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loadingMenu" class="status-card">
        <div class="spinner"></div>
        <p class="status-text">در حال بارگذاری منو...</p>
      </div>

      <!-- Empty State -->
      <div v-else-if="menuItems.length === 0" class="status-card empty-state">
        <div class="empty-icon">🍽️</div>
        <h3 class="empty-title">منوی شما خالی است</h3>
        <p class="empty-description">هنوز هیچ غذایی به منوی خود اضافه نکرده‌اید.</p>
      </div>

      <!-- Menu Table -->
      <div v-else class="table-wrapper">
        <table class="menu-table">
          <thead>
            <tr>
              <th>
                <span class="th-content">
                  <span class="th-icon">🖼️</span>
                  عکس
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">🏷️</span>
                  نام غذا
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">💰</span>
                  قیمت
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">📂</span>
                  دسته‌بندی
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">✅</span>
                  وضعیت
                </span>
              </th>
              <th>
                <span class="th-content">
                  <span class="th-icon">⚙️</span>
                  عملیات
                </span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in menuItems" :key="item.id" class="menu-row">
              <td class="image-cell">
                <img :src="getFullImageUrl(item.image)" :alt="item.name" class="food-image">
              </td>
              <td class="name-cell">
                <span class="food-name">{{ item.name }}</span>
              </td>
              <td class="price-cell">
                <span class="food-price">{{ parseFloat(item.price).toLocaleString('fa-IR') }} تومان</span>
              </td>
              <td class="category-cell">
                <span class="category-badge">{{ item.category?.name || '---' }}</span>
              </td>
              <td class="status-cell">
                <span :class="['status-badge', item.is_available ? 'available' : 'unavailable']">
                  {{ item.is_available ? 'موجود' : 'ناموجود' }}
                </span>
              </td>
              <td class="actions-cell">
                <button class="action-btn edit-btn" @click="openEditModal(item)">
                  <span class="btn-icon">✏️</span>
                  ویرایش
                </button>
                <button class="action-btn delete-btn" @click="deleteItem(item.id)">
                  <span class="btn-icon">🗑️</span>
                  حذف
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- مودال ویرایش آیتم -->
    <EditFoodItemModal
      v-if="isModalVisible"
      :item-to-edit="selectedItem"
      :categories="categories"
      @close="isModalVisible = false"
      @item-updated="handleItemUpdate"
    />
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import managerService from '../services/managerService';
import EditFoodItemModal from '../components/EditFoodItemModal.vue';

const categories = ref([]);
const menuItems = ref([]);
const loadingMenu = ref(true);
const isModalVisible = ref(false);
const selectedItem = ref(null);

const newFood = reactive({
  name: '',
  description: '',
  price: '',
  category: '',
  is_available: true,
});

const getFullImageUrl = (imagePath) => {
  if (!imagePath) return '/placeholder.png'; // یک عکس پیش‌فرض
  if (imagePath.startsWith('http')) {
    return imagePath;
  }
  return `http://127.0.0.1:8000${imagePath}`;
};

const fetchInitialData = async () => {
  loadingMenu.value = true;
  try {
    const [catResponse, menuResponse] = await Promise.all([
      managerService.getCategories(),
      managerService.getRestaurantMenu()
    ]);
    categories.value = catResponse.data;
    menuItems.value = menuResponse.data;
  } catch (error) {
    console.error("Failed to fetch initial data:", error);
    alert('خطا در دریافت اطلاعات اولیه.');
  } finally {
    loadingMenu.value = false;
  }
};

const addFoodItem = async () => {
  try {
    await managerService.createFoodItem({ ...newFood });
    alert('غذای جدید با موفقیت اضافه شد.');
    Object.assign(newFood, { name: '', description: '', price: '', category: '', is_available: true });
    await fetchInitialData(); // رفرش لیست
  } catch (error) {
    console.error("Failed to add food item:", error);
    alert('خطا در افزودن غذا.');
  }
};

const deleteItem = async (foodId) => {
  if (confirm('آیا از حذف این آیتم مطمئن هستید؟')) {
    try {
      await managerService.deleteFoodItem(foodId);
      alert('آیتم با موفقیت حذف شد.');
      await fetchInitialData(); // رفرش لیست
    } catch (error) {
      console.error("Failed to delete item:", error);
      alert('خطا در حذف آیتم.');
    }
  }
};

const openEditModal = (item) => {
  selectedItem.value = { ...item }; // یک کپی از آیتم می‌سازیم تا تغییرات مستقیم اعمال نشود
  isModalVisible.value = true;
};

const handleItemUpdate = async (updatedItem) => {
  try {
    // یک کپی از داده‌ها می‌سازیم
    const dataToUpdate = { ...updatedItem };
    
    // فیلد image را از داده‌هایی که قرار است ارسال شود حذف می‌کنیم
    delete dataToUpdate.image;
    
    // حالا داده‌های تمیز شده را به سرویس ارسال می‌کنیم
    await managerService.updateFoodItem(updatedItem.id, dataToUpdate);
    
    alert('آیتم با موفقیت به‌روزرسانی شد.');
    isModalVisible.value = false;
    await fetchInitialData(); // رفرش لیست
  } catch (error) {
    console.error("Failed to update item:", error.response?.data);
    // حالا می‌توانیم خطای دقیق‌تری نمایش دهیم
    const errorMessages = JSON.stringify(error.response?.data);
    alert(`خطا در به‌روزرسانی آیتم: ${errorMessages}`);
  }
};

onMounted(fetchInitialData);
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap");

/* Base Styles */
.manager-menu-page {
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
  animation: rotate 4s ease-in-out infinite;
}

@keyframes rotate {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-10deg); }
  75% { transform: rotate(10deg); }
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

/* Section Styles */
.add-food-section,
.menu-list-section {
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

.menu-count {
  background: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

/* Form Styles */
.add-food-form {
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.full-width {
  grid-column: 1 / -1;
}

.form-label {
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

.form-input,
.form-select,
.form-textarea {
  padding: 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 1rem;
  font-family: inherit;
  transition: all 0.3s ease;
  background: #ffffff;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: #dc143c;
  box-shadow: 0 0 0 3px rgba(220, 20, 60, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

/* Toggle Switch */
.status-toggle {
  display: flex;
  align-items: center;
  height: 54px;
}

.toggle-label {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
}

.toggle-input {
  display: none;
}

.toggle-slider {
  width: 50px;
  height: 26px;
  background: #ccc;
  border-radius: 26px;
  position: relative;
  transition: background 0.3s ease;
}

.toggle-slider::before {
  content: '';
  position: absolute;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #ffffff;
  top: 2px;
  right: 2px;
  transition: transform 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-input:checked + .toggle-slider {
  background: #dc143c;
}

.toggle-input:checked + .toggle-slider::before {
  transform: translateX(-24px);
}

.toggle-text {
  font-weight: 600;
  color: #dc143c;
}

/* Submit Button */
.submit-btn {
  background: linear-gradient(135deg, #dc143c 0%, #b71c1c 100%);
  color: #ffffff;
  border: none;
  border-radius: 12px;
  padding: 16px 32px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(220, 20, 60, 0.2);
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(220, 20, 60, 0.3);
}

.btn-icon {
  font-size: 1.2rem;
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

.menu-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 1rem;
}

.menu-table thead tr {
  background: #f8f9fa;
  border-bottom: 2px solid #dc143c;
}

.menu-table th {
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

.menu-row {
  transition: all 0.3s ease;
  border-bottom: 1px solid #f0f0f0;
}

.menu-row:nth-child(even) {
  background: #fafafa;
}

.menu-row:hover {
  background: linear-gradient(90deg, rgba(220, 20, 60, 0.05) 0%, rgba(220, 20, 60, 0.02) 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 20, 60, 0.1);
}

.menu-table td {
  padding: 20px 16px;
  text-align: right;
  vertical-align: middle;
}

/* Table Cell Specific Styles */
.image-cell {
  text-align: center;
}

.food-image {
  width: 70px;
  height: 70px;
  object-fit: cover;
  border-radius: 12px;
  border: 2px solid #dc143c;
  box-shadow: 0 2px 8px rgba(220, 20, 60, 0.1);
}

.food-name {
  font-weight: 600;
  font-size: 1.1rem;
  color: #333333;
}

.food-price {
  font-weight: 700;
  font-size: 1rem;
  color: #dc143c;
}

.category-badge {
  background: rgba(220, 20, 60, 0.1);
  color: #dc143c;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  border: 1px solid rgba(220, 20, 60, 0.2);
}

.status-badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  border: 1px solid;
}

.status-badge.available {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border-color: rgba(34, 197, 94, 0.2);
}

.status-badge.unavailable {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
  border-color: rgba(239, 68, 68, 0.2);
}

/* Action Buttons */
.actions-cell {
  display: flex;
  gap: 8px;
  justify-content: center;
}

.action-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.3s ease;
}

.edit-btn {
  background: #fbbf24;
  color: #000000;
}

.edit-btn:hover {
  background: #f59e0b;
  transform: translateY(-1px);
}

.delete-btn {
  background: #ef4444;
  color: #ffffff;
}

.delete-btn:hover {
  background: #dc2626;
  transform: translateY(-1px);
}

/* Responsive Design */
@media (max-width: 768px) {
  .manager-menu-page {
    padding: 24px 16px;
  }

  .page-header {
    padding: 40px 20px;
  }

  .page-title {
    font-size: 2.2rem;
  }

  .form-row {
    grid-template-columns: 1fr;
    gap: 20px;
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

  .add-food-form {
    padding: 24px;
  }

  .menu-table th,
  .menu-table td {
    padding: 12px 8px;
    font-size: 0.9rem;
  }

  .actions-cell {
    flex-direction: column;
    gap: 4px;
  }

  .action-btn {
    font-size: 0.8rem;
    padding: 6px 12px;
  }

  .food-image {
    width: 50px;
    height: 50px;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.8rem;
  }

  .section-title {
    font-size: 1.3rem;
  }

  .menu-table {
    font-size: 0.8rem;
  }

  .food-image {
    width: 40px;
    height: 40px;
  }
}
</style>