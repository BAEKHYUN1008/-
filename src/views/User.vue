<template>
  <div class="user-center">
    <el-tabs v-model="activeTab">
      <el-tab-pane label="我的订阅" name="subscription">
        <el-table :data="subscriptions" style="width: 100%">
          <el-table-column prop="type" label="订阅类型" />
          <el-table-column prop="content" label="订阅内容" />
          <el-table-column prop="status" label="状态">
            <template #default="{ row }">
              <el-tag :type="row.status === '已启用' ? 'success' : 'info'">{{ row.status }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default>
              <el-button link type="primary">编辑</el-button>
              <el-button link type="danger">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-button type="primary" style="margin-top: 20px">+ 添加订阅</el-button>
      </el-tab-pane>

      <el-tab-pane label="消息通知" name="notification">
        <el-table :data="notifications" style="width: 100%">
          <el-table-column prop="title" label="标题" />
          <el-table-column prop="status" label="状态" width="100">
            <template #default="{ row }">
              <el-tag :type="row.status === '未读' ? 'danger' : 'info'">{{ row.status }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="time" label="时间" width="150" />
        </el-table>
        <el-button link style="margin-top: 10px">全部标记为已读</el-button>
      </el-tab-pane>

      <el-tab-pane label="搜索历史" name="history">
        <el-tag v-for="h in history" :key="h" style="margin: 5px">{{ h }}</el-tag>
      </el-tab-pane>

      <el-tab-pane label="设置" name="settings">
        <el-form label-width="100px">
          <el-form-item label="通知方式">
            <el-checkbox-group v-model="settings.notify">
              <el-checkbox label="邮件">邮件</el-checkbox>
              <el-checkbox label="站内信">站内信</el-checkbox>
            </el-checkbox-group>
          </el-form-item>
          <el-form-item>
            <el-button type="primary">保存设置</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('subscription')

const subscriptions = ref([
  { type: '按时效', content: '新法规发布', status: '已启用' },
  { type: '按部门', content: '中国民用航空局', status: '已启用' },
  { type: '按分类', content: '航空器管理', status: '已启用' }
])

const notifications = ref([
  { title: '《低空经济政策》已发布', status: '未读', time: '03-12 10:30' },
  { title: '《飞行安全规范》已更新', status: '已读', time: '03-10 15:20' }
])

const history = ref(['通用航空管理办法', '低空经济政策', '飞行安全规范'])

const settings = ref({ notify: ['邮件'] })
</script>

<style scoped>
.user-center { background: white; padding: 20px; border-radius: 8px; }
</style>