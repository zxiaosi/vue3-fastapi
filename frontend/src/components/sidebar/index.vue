<script setup lang="ts">
import { computed, onMounted, reactive, ref } from "vue";
import { useStore } from "@/stores";
import { useRoute, useRouter, type RouteRecordRaw, type _RouteRecordBase } from "vue-router";

const store = useStore(); // 状态管理
const route = useRoute(); // 操作路由
const router = useRouter(); // 全局路由

// 当前路由
const onRoutes = computed(() => {
  return route.path;
});

const state = reactive({
  routers: [] as any,
});

onMounted(() => {
  router.options.routes.map((item) => {
    if (item.name == "home") {
      state.routers = item.children;
    } else {
      return;
    }
  });
});
</script>

<template>
  <div class="sidebar">
    <el-menu
      class="sidebar-el-menu"
      :default-active="onRoutes"
      :collapse="store.collapse"
      background-color="#324157"
      text-color="#bfcbd9"
      active-text-color="#20a0ff"
      unique-opened
      router
    >
      <template v-for="item in state.routers">
        <!-- 二级标题 -->
        <template v-if="item.children">
          <el-sub-menu :index="item.path">
            <template #title>
              <el-icon :class="item.meta.icon" />
              <span>{{ item.meta.title }}</span>
            </template>

            <template v-for="subItem in item.children">
              <el-menu-item :index="subItem.path">{{ subItem.meta.title }}</el-menu-item>
            </template>
          </el-sub-menu>
        </template>

        <!-- 一级标题 -->
        <template v-else>
          <el-menu-item :index="item.path">
            <el-icon :class="item.meta.icon" />
            <template #title>{{ item.meta.title }}</template>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<style scoped>
.sidebar {
  display: block;
  position: absolute;
  left: 0;
  top: 70px;
  bottom: 0;
  overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
  width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
  width: 250px;
}

.sidebar > ul {
  height: 100%;
}
</style>
