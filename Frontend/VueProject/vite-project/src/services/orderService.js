// src/services/orderService.js
import apiClient from './api';

export default {
  getMyOrders() {
    // URL بر اساس کدی که هم‌تیمی شما نوشته
    return apiClient.get('/orders/my/'); 
  }
};