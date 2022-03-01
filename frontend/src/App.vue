<script setup lang="ts">
import { provide } from "vue";
import * as echarts from "echarts";
// provide/inject 声明类型: https://www.jianshu.com/p/7064c5f8f143

// 声明echarts (依赖注入)
provide("echarts", echarts);
</script>

<template>
  <router-view />
</template>

<style>
@import "@/assets/css/main.css";
@import "@/assets/css/color-dark.css";
</style>
