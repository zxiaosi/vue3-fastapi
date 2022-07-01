<script setup lang="ts">
import { useStore } from "@/stores";
import vHeader from "@/layout/Header/index.vue";
import vSidebar from "@/layout/Sidebar/index.vue";
import vTags from "@/layout/Tags/index.vue";

const store = useStore(); // 状态管理

// 标签名字列表
const tagsList = store.tagNameList;
</script>

<template>
  <div class="about">
    <v-header />
    <v-sidebar />

    <div class="content-box" :class="{ 'content-collapse': store.collapse }">
      <v-tags />
      <div class="content">
        <router-view v-slot="{ Component, route }">
          <transition name="MainFade" mode="out-in">
            <keep-alive :include="tagsList">
              <component :is="Component" :key="route.path" />
            </keep-alive>
          </transition>
        </router-view>
      </div>
    </div>
  </div>
</template>

<style>
.MainFade-enter-from,
.MainFade-leave-to {
  opacity: 0;
}
.MainFade-enter-to,
.MainFade-leave-from {
  opacity: 1;
}
.MainFade-enter-active,
.MainFade-leave-active {
  transition: opacity 0.3s;
}
</style>
