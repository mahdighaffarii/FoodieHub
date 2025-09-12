// src/services/restaurantService.js
import apiClient from './api';

export default {
  getRestaurants() {
    return apiClient.get('/restaurants/');
  },
  getRestaurantDetail(id) {
    return apiClient.get(`/restaurants/${id}/`);
  }
};