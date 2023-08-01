<script setup lang="ts">
import { RouterView } from "vue-router";
import zhCn from "element-plus/dist/locale/zh-cn.mjs"; // element-plus 中文语言包
</script>

<template>
  <el-config-provider :locale="zhCn">
    <RouterView />
  </el-config-provider>
</template>

<style></style>
