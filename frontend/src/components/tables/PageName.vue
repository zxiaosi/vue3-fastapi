<template>
  <!-- 页面标题 -->
  <div class="crumbs">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>
        <i :class="`el-icon-ali-${iconName}`" /> {{pageName}}表
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script setup>
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