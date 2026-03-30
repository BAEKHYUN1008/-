import request from '@/utils/request';
export function searchLaw(keyword) {
  return request.get('/search/', { params: { keyword } });
}