<template>
  <el-table :data="laws" style="width: 100%">
    <el-table-column prop="title" label="标题">
      <template #default="scope">
        <el-link type="primary" @click="$emit('view-detail', scope.row)">
          {{ scope.row.title }}
        </el-link>
      </template>
    </el-table-column>
    <el-table-column prop="publish_date" label="发布日期" width="150" />
  </el-table>
</template>

<script setup>
defineProps({
  laws: {
    type: Array,
    required: true
  }
})

defineEmits(['view-detail'])
</script>