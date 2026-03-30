<template>
  <div class="result">
    <!-- 筛选条件区域 -->
    <div class="filters">
      <div class="filter-row">
        <span class="label">分类：</span>
        <div class="filter-buttons">
          <el-button
            v-for="cat in categories"
            :key="cat"
            :type="selectedCategory === cat ? 'primary' : 'default'"
            size="small"
            @click="selectedCategory = cat"
          >
            {{ cat }}
          </el-button>
        </div>
      </div>

      <div class="filter-row">
        <span class="label">发布时间：</span>
        <div class="filter-buttons">
          <el-button
            v-for="time in timeRanges"
            :key="time"
            :type="selectedTime === time ? 'primary' : 'default'"
            size="small"
            @click="selectedTime = time"
          >
            {{ time }}
          </el-button>
          <el-date-picker
            v-model="customDate"
            type="daterange"
            size="small"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            v-if="selectedTime === '自定义'"
          />
        </div>
      </div>

      <div class="filter-row">
        <span class="label">排序：</span>
        <div class="filter-buttons">
          <el-button
            v-for="sort in sortOptions"
            :key="sort"
            :type="selectedSort === sort ? 'primary' : 'default'"
            size="small"
            @click="selectedSort = sort"
          >
            {{ sort }}
          </el-button>
        </div>
      </div>

      <div class="result-count">共找到 {{ total }} 条结果</div>
    </div>

    <!-- 搜索结果列表 -->
    <div class="result-list">
      <div v-for="item in lawList" :key="item.id" class="result-item">
        <div class="item-title">
          <el-link type="primary" @click="goToDetail(item)">{{ item.title }}</el-link>
        </div>
        <div class="item-meta">
          <span>发文部门：{{ item.department }}</span>
          <span>发布日期：{{ item.publishDate }}</span>
        </div>
        <div class="item-summary" v-html="item.summary"></div>
        <div class="item-actions">
          <el-button link type="primary" @click="goToDetail(item)">查看详情</el-button>
          <el-button link type="primary">下载PDF</el-button>
        </div>
      </div>
    </div>

    <!-- 分页 -->
    <div class="pagination">
      <el-pagination
        v-model:current-page="currentPage"
        :page-size="pageSize"
        :total="total"
        layout="prev, pager, next"
        @current-change="handlePageChange"
      />
    </div>

    <!-- 法规详情弹窗 -->
    <el-dialog v-model="dialogVisible" :title="currentLaw.title" width="60%">
      <div class="law-detail">
        <div class="law-meta">
          <p><strong>发文部门：</strong>{{ currentLaw.department }}</p >
          <p><strong>发布日期：</strong>{{ currentLaw.publishDate }}</p >
          <p><strong>生效日期：</strong>{{ currentLaw.effectiveDate }}</p >
          <p><strong>文号：</strong>{{ currentLaw.docNumber }}</p >
        </div>
        <div class="law-content" v-html="currentLaw.content"></div>
        <div class="law-actions">
          <el-button type="primary">下载PDF</el-button>
          <el-button>订阅通知</el-button>
          <el-button>收藏</el-button>
        </div>
        <div class="rag-interpretation">
          <h4>RAG通俗解读</h4>
          <p>{{ currentLaw.interpretation }}</p >
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

// 筛选条件
const categories = ['全部', '航空器管理', '飞行安全', '运行监管', '空域使用']
const timeRanges = ['全部', '近7天', '近30天', '近90天', '自定义']
const sortOptions = ['相关度', '最新', '最热']

const selectedCategory = ref('全部')
const selectedTime = ref('全部')
const selectedSort = ref('相关度')
const customDate = ref(null)
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(156)

// 弹窗
const dialogVisible = ref(false)
const currentLaw = ref({})

// 模拟数据
const lawList = ref([
  {
    id: 1,
    title: '《通用航空飞行管理办法》',
    department: '中国民用航空局',
    publishDate: '2024-01-15',
    effectiveDate: '2024-02-01',
    docNumber: '民航局令第XX号',
    summary: '为规范<em>通用航空</em>飞行活动，保障飞行安全...',
    content: '第一章 总则<br/>第一条 为规范通用航空飞行活动，保障飞行安全...<br/>第二条 本办法适用于...',
    interpretation: '这部法规主要规定了通用航空飞行的申请流程、安全要求和监管措施。通俗来说，就是告诉你怎么合法合规地飞。'
  },
  {
    id: 2,
    title: '《通用航空器适航管理规定》',
    department: '中国民用航空局',
    publishDate: '2023-12-20',
    effectiveDate: '2024-01-20',
    docNumber: '民航局令第XX号',
    summary: '加强对<em>通用航空器</em>的适航管理...',
    content: '第一章 总则<br/>第一条 为加强通用航空器适航管理...',
    interpretation: '这部法规主要规定了航空器必须符合的安全标准。'
  }
])

const goToDetail = (item) => {
  currentLaw.value = item
  dialogVisible.value = true
}

const handlePageChange = (page) => {
  currentPage.value = page
  // 这里可以重新加载数据
}

onMounted(() => {
  const query = route.query.q
  if (query) {
    // 如果有搜索关键词，可以在这里调用搜索接口
    console.log('搜索关键词:', query)
  }
})
</script>

<style scoped>
.result {
  max-width: 1200px;
  margin: 0 auto;
}

.filters {
  background: white;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
}

.filter-row {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  flex-wrap: wrap;
}

.label {
  width: 80px;
  color: #666;
}

.filter-buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.result-count {
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #e4e7ed;
  color: #666;
}

.result-list {
  background: white;
  border-radius: 12px;
  padding: 20px;
}

.result-item {
  padding: 20px;
  border-bottom: 1px solid #e4e7ed;
}

.result-item:last-child {
  border-bottom: none;
}

.item-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.item-meta {
  display: flex;
  gap: 20px;
  color: #999;
  font-size: 13px;
  margin-bottom: 10px;
}

.item-summary {
  color: #666;
  line-height: 1.6;
  margin-bottom: 10px;
}

.item-actions {
  display: flex;
  gap: 15px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.law-detail {
  max-height: 500px;
  overflow-y: auto;
}

.law-meta {
  background: #f5f7fa;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.law-meta p {
  margin: 5px 0;
}

.law-content {
  line-height: 1.8;
  margin-bottom: 20px;
}

.law-actions {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.rag-interpretation {
  background: #e6f7ff;
  padding: 15px;
  border-radius: 8px;
  margin-top: 20px;
}

.rag-interpretation h4 {
  margin-bottom: 10px;
  color: #409eff;
}
</style>