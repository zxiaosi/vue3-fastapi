<script setup lang="ts">
import { computed } from "vue";
import { useStore } from "@/stores";
import { useRoute, useRouter, onBeforeRouteUpdate } from "vue-router";
import { Close, ArrowDown } from "@element-plus/icons-vue";

const store = useStore(); // 状态管理
const route = useRoute(); // 路由对象
const router = useRouter(); // 全局路由

// 当前路由是否活跃
const isActive = (path: string): boolean => {
  return path === route.fullPath;
};

// 获取标签列表
const showTags = computed((): boolean => store.tagsList.length > 0);

/**
 * 关闭单个标签
 * @param index 当前标签的索引
 */
const closeTags = (index: number) => {
  const delItem = store.tagsList[index];
  store.delTagsItem(index);
  const item = store.tagsList[index] ? store.tagsList[index] : store.tagsList[index - 1];
  if (item) {
    delItem.path === route.fullPath && router.push(item.path);
  } else {
    router.push("/");
  }
};

/**
 * 设置标签
 * @param route 路由对象
 */
const setTags = (route: any) => {
  const isExist = store.tagsList.some((item) => {
    return item.path === route.fullPath;
  });
  if (!isExist) {
    if (store.tagsList.length >= 8) {
      store.delTagsItem(0);
    }
    store.setTagsItem({
      name: route.name,
      title: route.meta.title,
      path: route.fullPath,
    });
  }
};

setTags(route);
onBeforeRouteUpdate((to) => {
  setTags(to);
});

// 关闭全部标签
const closeAll = () => {
  store.clearTags();
  router.push("/");
};

// 关闭其他标签
const closeOther = () => {
  const currentItem = store.tagsList.filter((item) => {
    return item.path === route.fullPath;
  });
  store.closeTagsOther(currentItem);
};

// 标签操作
const handleTags = (command: string) => {
  command === "other" ? closeOther() : closeAll();
};
</script>

<template>
  <div class="tags" v-if="showTags">
    <!-- 标签列表 -->
    <ul>
      <li class="tags-li" v-for="(item, index) in store.tagsList" :class="{ active: isActive(item.path) }" :key="index">
        <router-link :to="item.path" class="tags-li-title">{{ item.title }}</router-link>
        <span class="tags-li-icon" @click="closeTags(index)">
          <el-icon color="#606266"><close /></el-icon>
        </span>
      </li>
    </ul>

    <!-- 标签选项 -->
    <div class="tags-close-box">
      <el-dropdown @command="handleTags">
        <el-button size="small" type="primary">
          <span>标签选项</span>
          <el-icon class="el-icon--right"><arrow-down /></el-icon>
        </el-button>

        <template #dropdown>
          <el-dropdown-menu size="small">
            <el-dropdown-item command="other">关闭其他</el-dropdown-item>
            <el-dropdown-item command="all">关闭所有</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<style>
.tags {
  position: relative;
  height: 30px;
  overflow: hidden;
  background: #fff;
  padding-right: 120px;
  box-shadow: 0 5px 10px #ddd;
}

.tags ul {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.tags-li {
  float: left;
  margin: 3px 5px 2px 3px;
  border-radius: 3px;
  font-size: 12px;
  overflow: hidden;
  cursor: pointer;
  height: 23px;
  line-height: 23px;
  border: 1px solid #e9eaec;
  background: #fff;
  padding: 0 5px 0 12px;
  vertical-align: middle;
  color: #666;
  -webkit-transition: all 0.3s ease-in;
  -moz-transition: all 0.3s ease-in;
  transition: all 0.3s ease-in;
}

.tags-li:not(.active):hover {
  background: #f8f8f8;
}

.tags-li.active {
  color: #fff;
}

.tags-li-title {
  float: left;
  max-width: 80px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-right: 5px;
  color: #666;
}

.tags-li.active .tags-li-title {
  color: #fff;
}

/* 标签后面的关闭图标 */
.tags-li-icon .el-icon {
  padding-top: 4px;
}

.tags-close-box {
  position: absolute;
  right: 0;
  top: 3px;
  box-sizing: border-box;
  text-align: center;
  width: 110px;
  height: 30px;
  line-height: 28px;
  background: #fff;
  box-shadow: -3px 0 15px 3px rgba(0, 0, 0, 0.1);
  z-index: 10;
}
</style>
