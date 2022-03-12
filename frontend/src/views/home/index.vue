<script setup lang="ts">
import { useStore } from "@/stores";
import vHeader from "@/components/header/index.vue";
import vSidebar from "@/components/sidebar/index.vue";
import vTags from "@/components/tags/index.vue";

// 状态管理
const store = useStore();

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
        <router-view v-slot="{ Component }">
          <keep-alive :include="tagsList">
            <component :is="Component" />
          </keep-alive>
        </router-view>
      </div>
    </div>
  </div>
</template>
