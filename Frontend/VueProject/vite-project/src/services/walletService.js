// src/services/walletService.js
import apiClient from './api';

export default {
  getWalletHistory() {
    return apiClient.get('/wallets/history/');
  }
};