import apiClient from './api';

export default {
  // --- Order Management ---
  getRestaurantOrders() {
    return apiClient.get('/orders/restaurant/');
  },
  updateOrderStatus(orderId, newStatus) {
    return apiClient.patch(`/orders/${orderId}/update-status/`, { status: newStatus });
  },

  createFoodItem(foodData) {
    return apiClient.post('/restaurants/foods/create/', foodData);
  },
  getCategories() {
    return apiClient.get('/restaurants/categories/');
  },
  getRestaurantMenu() {
    return apiClient.get('/restaurants/foods/my-menu/');
  },
  deleteFoodItem(foodId) {
    return apiClient.delete(`/restaurants/foods/${foodId}/`);
  },
  updateFoodItem(foodId, foodData) {
  // DRF برای Update از متد PUT یا PATCH استفاده می‌کند
  return apiClient.patch(`/restaurants/foods/${foodId}/`, foodData);
},
  getSalesReport(params) {
    // params می‌تواند { period: 'daily' } یا { start_date: '...', end_date: '...' } باشد
    return apiClient.get('/orders/restaurant/report/', { params });
  },
    createRestaurant(restaurantData) {
    return apiClient.post('/restaurants/create/', restaurantData);
  }
};