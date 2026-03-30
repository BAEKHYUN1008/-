<template>
  <div class="home">
    <div class="search-section">
      <h1>法规知识库</h1>
      <el-input v-model="keyword" placeholder="请输入关键词搜索..." size="large" class="search-input" @keyup.enter="search">
        <template #append>
          <el-button type="primary" @click="search">搜索</el-button>
        </template>
      </el-input>
      <div class="hot-search">
        <span>热门搜索：</span>
        <el-link v-for="item in hotSearches" :key="item" @click="keyword = item; search()">{{ item }}</el-link>
      </div>
    </div>

    <div class="categories">
      <h3>法规分类</h3>
      <div class="category-list">
        <div v-for="cat in categories" :key="cat.name" class="category-item" @click="keyword = cat.name; search()">
          <span>{{ cat.name }}</span>
          <span class="count">{{ cat.count }}</span>
        </div>
      </div>
    </div>

    <div class="latest-updates">
      <h3>最新法规更新</h3>
      <el-timeline>
        <el-timeline-item v-for="item in latestLaws" :key="item.title" :timestamp="item.date">
          <el-link @click="goToDetail(item.title)">{{ item.title }}</el-link>
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const keyword = ref('')

const hotSearches = ['通用航空管理办法', '低空经济政策', '飞行安全规范']

const categories = ref([
  { name: '航空器管理', count: 120 },
  { name: '飞行安全', count: 85 },
  { name: '运行监管', count: 95 },
  { name: '空域使用', count: 63 }
])

const latestLaws = ref([
  { title: '《通用航空飞行管理办法》', date: '2025-03-01' },
  { title: '《低空经济产业发展指导意见》', date: '2025-02-28' },
  { title: '《民用航空器适航管理规定》', date: '2025-02-25' }
])

const search = () => {
  if (keyword.value) router.push(`/result?q=${keyword.value}`)
}

const goToDetail = (title) => {
  router.push(`/detail?title=${title}`)
}
</script>

<style scoped>
.home { max-width: 1200px; margin: 0 auto; }
.search-section { text-align: center; margin-bottom: 40px; padding: 40px 20px; background: white; border-radius: 12px; }
.search-input { width: 600px; margin-top: 20px; }
.hot-search { margin-top: 15px; display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; }
.categories { background: white; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
.category-list { display: flex; gap: 20px; flex-wrap: wrap; margin-top: 15px; }
.category-item { background: #f5f7fa; padding: 10px 20px; border-radius: 8px; display: flex; gap: 10px; cursor: pointer; }
.count { color: #409eff; font-weight: bold; }
.latest-updates { background: white; border-radius: 12px; padding: 20px; }
</style>