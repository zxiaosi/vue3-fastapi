<template>
  <div class="sidebar">
    <el-menu class="sidebar-el-menu" :default-active="onRoutes" :collapse="collapse"
      background-color="#324157" text-color="#bfcbd9" active-text-color="#20a0ff" unique-opened
      router>
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-sub-menu :index="item.index" :key="item.index">
            <template #title>
              <el-icon :class="item.icon" />
              <span>{{ item.title }}</span>
            </template>
            <template v-for="(subItem, index) in item.subs">
              <el-sub-menu v-if="subItem.subs" :index="subItem.index" :key="subItem.index">
                <template #title>{{ subItem.title }}</template>
                <el-menu-item v-for="(threeItem, i) in subItem.subs" :key="i"
                  :index="threeItem.index">
                  {{ threeItem.title }}
                </el-menu-item>
              </el-sub-menu>
              <el-menu-item v-else :index="subItem.index" :key="index">{{ subItem.title }}
              </el-menu-item>
            </template>
          </el-sub-menu>
        </template>
        <template v-else>
          <el-menu-item :index="item.index" :key="item.index">
            <el-icon :class="item.icon" />
            <template #title>{{ item.title }}</template>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

// 侧边栏
const items = [
  { icon: 'el-icon-ali-home', index: '/dashboard', title: '系统首页' },
  {
    icon: 'el-icon-ali-cascades',
    index: '2',
    title: '信息表格',
    subs: [
      { index: '/department', title: '院系表' },
      { index: '/major', title: '专业表' },
      { index: '/teacher', title: '教师表' },
      { index: '/student', title: '学生表' },
      { index: '/course', title: '课程表' },
      { index: '/selectcourse', title: '选课表' },
      { index: '/basetable', title: '基础表格' },
    ],
  },
  { icon: 'el-icon-ali-copy', index: '/tabs', title: 'tab选项卡' },
  {
    icon: 'el-icon-ali-calendar',
    index: '3',
    title: '表单相关',
    subs: [{ index: '/baseform', title: '基本表单' }],
  },
  {
    icon: 'el-icon-ali-warn',
    index: '4',
    title: '错误处理',
    subs: [
      { index: '/permission', title: '权限测试' },
      { index: '/404', title: '404页面' },
    ],
  },
  { icon: 'el-icon-ali-test', index: '/test', title: '测试页面' },
];

const route = useRoute();

const onRoutes = computed(() => {
  return route.path;
});

const store = useStore();
const collapse = computed(() => store.state.collapse); // 折叠侧边栏

// defineExpose 可以省略
defineExpose({
  items,
  onRoutes,
  collapse,
});
</script>

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
