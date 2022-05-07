import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";
import Home from "@/views/home/index.vue";
import Tables from "@/views/tables/index.vue";
import Form from "@/views/form/index.vue";
import error from "@/views/40x/index.vue";
import { TITLE } from "@/assets/global";
import { getLocal } from "@/request/auth";

const routes: RouteRecordRaw[] = [
  { path: "/", redirect: "/dashboard" }, // 重定向
  {
    path: "/",
    name: "home",
    component: Home,
    children: [
      {
        path: "/dashboard",
        name: "dashboard",
        meta: { title: "系统首页", icon: "el-icon-ali-home", roles: ['admin', 'teacher', 'student'] },
        component: () => import("../views/dashboard/index.vue"),
      },
      {
        path: "/table",
        name: "table",
        meta: { title: "表格相关", icon: "el-icon-ali-cascades", roles: ['admin'] },
        component: Tables,
        children: [
          {
            path: "/department",
            name: "department", // 请求接口路径参数
            meta: { title: "院系表" },
            component: () => import("../views/tables/department/index.vue"),
          },
          {
            path: "/major",
            name: "major",
            meta: { title: "专业表" },
            component: () => import("../views/tables/major/index.vue"),
          },
          {
            path: "/teacher",
            name: "teacher",
            meta: { title: "教师表" },
            component: () => import("../views/tables/teacher/index.vue"),
          },
          {
            path: "/student",
            name: "student",
            meta: { title: "学生表" },
            component: () => import("../views/tables/student/index.vue"),
          },
          {
            path: "/course",
            name: "course",
            meta: { title: "课程表" },
            component: () => import("../views/tables/course/index.vue"),
          },
          {
            path: "/selectCourse",
            name: "selectCourse",
            meta: { title: "选课表" },
            component: () => import("../views/tables/selectCourse/index.vue"),
          },
        ],
      },
      {
        path: "/tabs",
        name: "tabs",
        meta: { title: "tab标签", icon: "el-icon-ali-copy", roles: ['admin'] },
        component: () => import("../views/tabs/index.vue"),
      },
      {
        path: "/form",
        name: "form",
        meta: { title: "表单相关", icon: "el-icon-ali-calendar", roles: ['admin'] },
        component: Form,
        children: [
          {
            path: "/baseform",
            name: "baseform",
            meta: { title: "基本表单" },
            component: () => import("../views/form/baseForm/index.vue"),
          },
        ],
      },
      {
        path: "/permission",
        name: "permission",
        meta: { title: "权限管理", icon: "el-icon-ali-warn", roles: ['admin'] },
        component: () => import("../views/permission/index.vue"),
      },
      {
        path: "/error",
        name: "error",
        meta: { title: "错误处理", icon: "el-icon-ali-warn", roles: ['admin'] },
        component: error,
        children: [
          {
            path: "/404",
            name: "404",
            meta: { title: "找不到页面" },
            component: () => import("../views/40x/404/index.vue"),
          },
          {
            path: "/403",
            name: "403",
            meta: { title: "没有权限" },
            component: () => import("../views/40x/403/index.vue"),
          },
        ],
      },
      {
        path: '/user',
        name: 'user',
        meta: { title: '个人中心', icon: "el-icon-ali-cascades", roles: ['admin', 'teacher', 'student'] },
        component: () => import("../views/user/index.vue"),
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    meta: { title: "登录" },
    component: () => import("../views/login/index.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

// 全局路由守卫
router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} | ${TITLE}`; // 页面名
  const userInfo = JSON.parse(getLocal("userInfo"));
  const role = getLocal("role");
  if (!userInfo && to.path !== "/login") {
    next("/login");
  } else if (to.meta.roles) {
    let roles: any = to.meta.roles;
    // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
    roles.indexOf(role) > -1 ? next() : next("/403");
  } else {
    next();
  }
});

export default router;
