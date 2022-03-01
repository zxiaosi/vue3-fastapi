<script setup lang="ts">
import { computed, ref } from "vue";
import { useStore } from "@/stores";
import { useRoute } from "vue-router";

const store = useStore(); // 状态管理
const route = useRoute(); // 路由对象

const onRoutes = computed(() => {
  return route.path;
});

// 仅二级标题
interface itemsType {
  icon: string;
  index: string;
  title: string;
  subs?: {
    index: string;
    title: string;
  }[];
}

// 侧边栏
const items: itemsType[] = [
  { icon: "el-icon-ali-home", index: "/dashboard", title: "系统首页" },
  {
    icon: "el-icon-ali-cascades",
    index: "/inf",
    title: "信息表格",
    subs: [
      { index: "/department", title: "院系表" },
      { index: "/major", title: "专业表" },
      { index: "/teacher", title: "教师表" },
      { index: "/student", title: "学生表" },
      { index: "/course", title: "课程表" },
      { index: "/selectcourse", title: "选课表" },
    ],
  },
  { icon: "el-icon-ali-copy", index: "/tabs", title: "tab选项卡" },
  {
    icon: "el-icon-ali-calendar",
    index: "/form",
    title: "表单相关",
    subs: [{ index: "/baseform", title: "基本表单" }],
  },
  {
    icon: "el-icon-ali-warn",
    index: "/err",
    title: "错误处理",
    subs: [
      { index: "/permission", title: "权限测试" },
      { index: "/404", title: "404页面" },
    ],
  },
];
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
      <template v-for="item in items">
        <!-- 二级标题 -->
        <template v-if="item.subs">
          <el-sub-menu :index="item.index">
            <template #title>
              <el-icon :class="item.icon" />
              <span>{{ item.title }}</span>
            </template>
            <template v-for="subItem in item.subs">
              <el-menu-item :index="subItem.index">{{ subItem.title }}</el-menu-item>
            </template>
          </el-sub-menu>
        </template>

        <!-- 一级标题 -->
        <template v-else>
          <el-menu-item :index="item.index">
            <el-icon :class="item.icon" />
            <template #title>{{ item.title }}</template>
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
