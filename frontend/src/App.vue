<template>
  <!-- TODO -->
  <router-view v-slot="{ Component }">
    <transition>
      <keep-alive>
        <component :is="Component" />
      </keep-alive>
    </transition>
  </router-view>
</template>

<script setup>
import { provide } from '@vue/runtime-core';
import * as echarts from 'echarts';

// 全局声明echarts
provide('echart', echarts);
</script>

<style>
@import './assets/css/main.css';
@import './assets/css/color-dark.css';
</style>
