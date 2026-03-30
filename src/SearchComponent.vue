<template>
  <div>
    <input v-model="keyword" placeholder="输入关键词" @keyup.enter="handleSearch" />
    <button @click="handleSearch">搜索</button>
    <ul>
      <li v-for="law in results" :key="law.id">{{ law.title }}</li>
    </ul>
  </div>
</template>

<script>
import { searchLaw } from '@/api/search';
export default {
  data() {
    return { keyword: '', results: [] };
  },
  methods: {
    async handleSearch() {
      try {
        const res = await searchLaw(this.keyword);
        this.results = res.data;
      } catch (error) {
        console.error('搜索失败', error);
      }
    }
  }
};
</script>