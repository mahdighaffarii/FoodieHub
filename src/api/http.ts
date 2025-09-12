import axios from 'axios';
import { useAuthStore } from '@/store/auth.store';

const http = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,  // باید آدرس API بک‌اند را وارد کنید
});

http.interceptors.request.use((config) => {
  const auth = useAuthStore();
  const token = auth.accessToken;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  if (!config.headers['Idempotency-Key']) {
    config.headers['Idempotency-Key'] = crypto.randomUUID?.() ?? String(Date.now());
  }
  return config;
});

let refreshing: Promise<void> | null = null;
http.interceptors.response.use(
  (r) => r,
  async (error) => {
    const { response, config } = error || {};
    const auth = useAuthStore();
    if (response?.status === 401 && auth.refreshToken && !config._retry) {
      config._retry = true;
      refreshing ||= auth.refreshTokens(); 
      await refreshing;
      refreshing = null;
      return http(config);
    }
    throw error;
  }
);

export default http;
                