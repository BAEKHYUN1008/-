import request from '@/utils/request';
export function subscribe(scene) {
  return request.post('/subscribe/', { scene });
}