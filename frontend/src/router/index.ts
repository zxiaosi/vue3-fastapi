import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import { TITLE } from "@/assets/global";
import { getLocal } from "@/request/auth";

const routes = [
  { path: "/", redirect: "/dashboard" }, // 重定向
  {
    path: "/",
    name: "home",
    component: Home,
    children: [
      {
        path: "/dashboard",
        name: "dashboard",
        meta: { title: "系统首页" }, // 路由跳转用
        component: () => import("@/views/Dashboard.vue"),
      },
      {
        path: "/department",
        name: "department",
        meta: { title: "院系表" },
        component: () => import("@/views/tables/Department.vue"),
      },
      {
        path: "/major",
        name: "major",
        meta: { title: "专业表" },
        component: () => import("@/views/tables/Major.vue"),
      },
      {
        path: "/teacher",
        name: "teacher",
        meta: { title: "教师表" },
        component: () => import("@/views/tables/Teacher.vue"),
      },
      {
        path: "/student",
        name: "student",
        meta: { title: "学生表" },
        component: () => import("@/views/tables/Student.vue"),
      },
      {
        path: "/course",
        name: "course",
        meta: { title: "课程表" },
        component: () => import("@/views/tables/Course.vue"),
      },
      {
        path: "/selectCourse",
        name: "selectCourse",
        meta: { title: "选课表" },
        component: () => import("@/views/tables/SelectCourse.vue"),
      },
      {
        path: "/tabs",
        name: "tabs",
        meta: { title: "tab标签" },
        component: () => import("@/views/Tabs.vue"),
      },
      {
        path: "/baseform",
        name: "baseform",
        meta: { title: "基本表单" },
        component: () => import("@/views/BaseForm.vue"),
      },
      {
        path: "/permission",
        name: "permission",
        meta: { title: "权限管理", permission: true },
        component: () => import("@/views/Permission.vue"),
      },
      {
        path: "/404",
        name: "404",
        meta: { title: "找不到页面" },
        component: () => import("@/views/40x/404.vue"),
      },
      {
        path: "/403",
        name: "403",
        meta: { title: "没有权限" },
        component: () => import("@/views/40x/403.vue"),
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    meta: { title: "登录" },
    component: () => import("@/views/Login.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} | ${TITLE}`; // 页面名
  const role = getLocal("username");
  if (!role && to.path !== "/login") {
    next("/login");
  } else if (to.meta.permission) {
    // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
    role === "admin" ? next() : next("/403");
  } else {
    next();
  }
});

export default router;
