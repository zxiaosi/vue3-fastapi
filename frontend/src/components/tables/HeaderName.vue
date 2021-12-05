<template>
  <!-- 页面标题 -->
  <div class="crumbs">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>
        <i :class="`el-icon-ali-${iconName}`" /> {{pageName}}
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script setup>
import { defineProps } from '@vue/runtime-core';
const props = defineProps({
  iconName: String, // 图标名
  pageName: String, // 页面名
});

// 可以省略
defineExpose({
  iconName: props.iconName,
  pageName: props.pageName,
});
</script>

<style>
</style>