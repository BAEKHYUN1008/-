<template>
  <div class="app-container">
    <!-- 左侧菜单栏 -->
    <div class="sidebar" :class="{ collapsed: isCollapsed }">
      <div class="logo" @click="toggleSidebar">
        <el-icon :size="24" v-if="isCollapsed"><Menu /></el-icon>
        <span v-else>法规检索系统</span>
      </div>

      <el-menu
        :collapse="isCollapsed"
        :default-active="activeMenu"
        router
      >
        <el-menu-item index="/">
          <el-icon><House /></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="/result">
          <el-icon><Search /></el-icon>
          <span>法规检索</span>
        </el-menu-item>
        <el-menu-item index="/user">
          <el-icon><User /></el-icon>
          <span>用户中心</span>
        </el-menu-item>
        <el-menu-item index="/detail">
          <el-icon><Document /></el-icon>
          <span>法规详情</span>
        </el-menu-item>
      </el-menu>
    </div>

    <div class="main-content">
      <div class="top-bar">
        <div class="left">
          <el-icon :size="20" class="menu-btn" @click="toggleSidebar">
            <Fold v-if="!isCollapsed" />
            <Expand v-else />
          </el-icon>
        </div>
        <div class="right">
          <el-dropdown>
            <div class="user-info">
              <el-avatar :size="32" :icon="UserFilled" />
              <span class="username">张三</span>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>个人中心</el-dropdown-item>
                <el-dropdown-item divided>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </div>

      <div class="page-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { Fold, Expand, Menu, House, Search, User, UserFilled, Document } from '@element-plus/icons-vue'

const route = useRoute()
const isCollapsed = ref(false)
const toggleSidebar = () => { isCollapsed.value = !isCollapsed.value }
const activeMenu = computed(() => route.path)
</script>

<style scoped>
* { margin: 0; padding: 0; box-sizing: border-box; }
.app-container { display: flex; height: 100vh; width: 100%; }
.sidebar { width: 220px; background-color: #001529; transition: width 0.3s; display: flex; flex-direction: column; overflow: hidden; }
.sidebar.collapsed { width: 64px; }
.logo { height: 60px; display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; font-weight: bold; background-color: #002140; cursor: pointer; }
.main-content { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.top-bar { height: 60px; background-color: white; border-bottom: 1px solid #e4e7ed; display: flex; align-items: center; justify-content: space-between; padding: 0 20px; }
.menu-btn { cursor: pointer; }
.user-info { display: flex; align-items: center; gap: 8px; cursor: pointer; }
.page-content { flex: 1; overflow-y: auto; padding: 20px; background-color: #f0f2f5; }
</style>