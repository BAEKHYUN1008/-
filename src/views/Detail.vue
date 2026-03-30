<template>
  <div class="detail-page">
    <div class="back-link">
      <el-link @click="goBack">
        <el-icon><ArrowLeft /></el-icon> 返回搜索结果
      </el-link>
    </div>

    <div class="law-detail">
      <h1>{{ law.title }}</h1>

      <div class="law-meta">
        <div class="meta-row">
          <span><strong>发文部门：</strong>{{ law.department }}</span>
          <span><strong>发布日期：</strong>{{ law.publishDate }}</span>
        </div>
        <div class="meta-row">
          <span><strong>生效日期：</strong>{{ law.effectiveDate }}</span>
          <span><strong>文号：</strong>{{ law.docNumber }}</span>
        </div>
      </div>

      <div class="law-content" v-html="law.content"></div>

      <div class="law-actions">
        <el-button type="primary">
          <el-icon><Download /></el-icon> 下载PDF
        </el-button>
        <el-button>
          <el-icon><Bell /></el-icon> 订阅通知
        </el-button>
        <el-button>
          <el-icon><Star /></el-icon> 收藏
        </el-button>
      </div>

      <div class="rag-interpretation">
        <h3>RAG通俗解读</h3>
        <p>{{ law.interpretation }}</p >
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ArrowLeft, Download, Bell, Star } from '@element-plus/icons-vue'

const route = useRoute()
const router = useRouter()

const law = ref({
  title: '《通用航空飞行管理办法》',
  department: '中国民用航空局',
  publishDate: '2024-01-15',
  effectiveDate: '2024-02-01',
  docNumber: '民航局令第XX号',
  content: `
    <h4>第一章 总则</h4>
    <p>第一条 为规范通用航空飞行活动，保障飞行安全，维护飞行秩序，根据《中华人民共和国民用航空法》和《中华人民共和国飞行基本规则》，制定本办法。</p >
    <p>第二条 在中华人民共和国境内从事通用航空飞行活动，应当遵守本办法。</p >
    <p>第三条 通用航空飞行活动应当遵循安全第一、服务发展、分类管理的原则。</p >
    <h4>第二章 飞行申请</h4>
    <p>第八条 从事通用航空飞行活动的单位或者个人，应当按照规定向飞行管制部门提出飞行计划申请。</p >
    <p>第九条 飞行计划申请应当包括飞行任务、航空器型号、飞行时间、飞行区域、飞行高度等内容。</p >
  `,
  interpretation: '这部法规主要规定了通用航空飞行的申请流程、安全要求和监管措施。通俗来说，就是告诉你怎么合法合规地进行通用航空飞行，包括：谁可以飞、怎么申请、飞的时候要注意什么。'
})

const goBack = () => {
  router.back()
}

onMounted(() => {
  const title = route.query.title
  if (title) {
    // 如果有标题参数，可以根据标题加载对应的法规
    console.log('加载法规:', title)
  }
})
</script>

<style scoped>
.detail-page {
  max-width: 1000px;
  margin: 0 auto;
}

.back-link {
  margin-bottom: 20px;
}

.law-detail {
  background: white;
  border-radius: 12px;
  padding: 30px;
}

.law-detail h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #303133;
}

.law-meta {
  background: #f5f7fa;
  padding: 15px 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.meta-row {
  display: flex;
  gap: 40px;
  margin-bottom: 10px;
}

.meta-row:last-child {
  margin-bottom: 0;
}

.meta-row span {
  color: #606266;
}

.law-content {
  line-height: 1.8;
  margin-bottom: 30px;
}

.law-content h4 {
  margin: 20px 0 10px 0;
  color: #409eff;
}

.law-content p {
  margin: 10px 0;
}

.law-actions {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
  padding-bottom: 30px;
  border-bottom: 1px solid #e4e7ed;
}

.rag-interpretation {
  background: #e6f7ff;
  padding: 20px;
  border-radius: 8px;
}

.rag-interpretation h3 {
  margin-bottom: 15px;
  color: #409eff;
}

.rag-interpretation p {
  line-height: 1.8;
  color: #606266;
}
</style>