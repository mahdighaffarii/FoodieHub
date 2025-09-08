import http from './http';

export const login = (email: string, password: string) =>
  http.post('/api/accounts/login/', { email, password });

export const refresh = (refresh: string) =>
  http.post('/api/accounts/login/refresh/', { refresh });
                