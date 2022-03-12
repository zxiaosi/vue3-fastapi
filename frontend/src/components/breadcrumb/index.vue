<script setup lang="ts">
import { reactive } from "vue";
import { useRoute } from "vue-router";
import type { stateType } from ".";

const route = useRoute(); // 操作路由

const state: stateType = reactive({
  secondRouterMeta: route.matched[1].meta, // 二级目录的标题
  currentRouterMeta: route.meta, // 当前路由
});
</script>

<template>
  <!-- 页面标题 -->
  <div class="crumbs">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>
        <el-icon :class="state.secondRouterMeta.icon" />
        <span>&nbsp;{{ state.secondRouterMeta.title }}</span>
      </el-breadcrumb-item>

      <el-breadcrumb-item v-if="state.currentRouterMeta.title != state.secondRouterMeta.title">
        <span>{{ state.currentRouterMeta.title }}</span>
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>
