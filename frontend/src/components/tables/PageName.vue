<script setup lang="ts">
import type { pageType } from "@/types/table";

interface propsType {
  page: pageType;
}

const props = defineProps<propsType>(); // 页面属性
</script>

<template>
  <!-- 页面标题 -->
  <div class="crumbs">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>
        <i :class="`el-icon-ali-${props.page.icon}`" />
        <span>&nbsp;{{ props.page.zhName }}</span>
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>
