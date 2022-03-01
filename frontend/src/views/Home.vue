<script setup lang="ts">
import { useStore } from "@/stores";
import vHeader from "@/components/Header.vue";
import vSidebar from "@/components/Sidebar.vue";
import vTags from "@/components/Tags.vue";

const store = useStore(); // 状态管理

const tagsList = store.tagsList.map((item) => {
  return item.name;
});
</script>

<template>
  <div class="about">
    <v-header />
    <v-sidebar />
    <div class="content-box" :class="{ 'content-collapse': store.collapse }">
      <v-tags />
      <div class="content">
        <router-view v-slot="{ Component }">
          <keep-alive :include="tagsList">
            <component :is="Component" />
          </keep-alive>
        </router-view>
      </div>
    </div>
  </div>
</template>
