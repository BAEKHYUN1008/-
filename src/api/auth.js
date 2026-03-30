import request from '@/utils/request';
export function login(username, password) {
  return request.post('/login/', { username, password });
}
export function logout() {
  return request.post('/logout/');
}