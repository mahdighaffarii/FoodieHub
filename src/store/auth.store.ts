import { defineStore } from 'pinia';
import { login as apiLogin, refresh as apiRefresh } from '@/api/auth.api';

export const useAuthStore = defineStore('auth', {
  state: () => ({ accessToken: '', refreshToken: '' }),
  getters: { isLoggedIn: (s) => !!s.accessToken },
  actions: {
    async login(email: string, password: string) {
      const { data } = await apiLogin(email, password);
      this.accessToken = data.access;
      this.refreshToken = data.refresh;
    },
    async refreshTokens() {
      if (!this.refreshToken) return;
      const { data } = await apiRefresh(this.refreshToken);
      this.accessToken = data.access;
    },
    logout() { this.accessToken = ''; this.refreshToken = ''; }
  },
  persist: true
});
                