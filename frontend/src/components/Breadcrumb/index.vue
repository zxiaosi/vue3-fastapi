<script setup lang="ts">
import { reactive } from "vue";
import { useRoute } from "vue-router";

interface Meta {
  title?: string;
  icon?: string;
  roles?: string[];
}

const route = useRoute(); // 操作路由

const state = reactive({
  secondMeta: route.matched[1].meta as Meta, // 二级路由元信息
  currentMeta: route.meta as Meta, // 当前路由元信息
});
</script>

<template>
  <!-- 页面标题 -->
  <div class="crumbs">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>
        <el-icon :class="`el-icon-ali-${state.secondMeta.icon}`" />
        <span>&nbsp;{{ state.secondMeta.title }}</span>
      </el-breadcrumb-item>

      <el-breadcrumb-item v-if="state.currentMeta.title != state.secondMeta.title">
        <span>{{ state.currentMeta.title }}</span>
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>
