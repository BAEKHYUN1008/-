<template>
  <div class="search-box">
    <el-input
      v-model="searchText"
      :placeholder="placeholder"
      :size="size"
      @keyup.enter="onSearch"
    >
      <template #append>
        <el-button type="primary" @click="onSearch">搜索</el-button>
      </template>
    </el-input>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  placeholder: {
    type: String,
    default: '请输入关键词...'
  },
  size: {
    type: String,
    default: 'large'
  }
})

const emit = defineEmits(['search'])
const searchText = ref('')

const onSearch = () => {
  emit('search', searchText.value)
}
</script>