import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";
import Layout from "@/layout/Home/index.vue";
import { getLocal } from "@/request/auth";
import { TITLE } from "@/assets/js/global";

const routes: RouteRecordRaw[] = [
  { path: "/", redirect: "/dashboard" }, // 重定向
  {
    path: "/login",
    name: "Login",
    meta: { title: "登录" },
    component: () => import("@/views/login/index.vue"),
  },
  {
    path: "/",
    name: "Layout",
    component: Layout,
    children: [
      {
        path: "/dashboard",
        name: "Dashboard",
        meta: { title: "系统首页", icon: "dashboard", roles: ["admin", "teacher", "student"] },
        component: () => import("@/views/dashboard/index.vue"),
      },
      {
        path: "/settings",
        name: "Settings",
        meta: { title: "系统管理", icon: "setting", roles: ["admin", "teacher", "student"] },
        component: () => import("@/views/settings/index.vue"),
        children: [
          {
            path: "/department",
            name: "Department",
            meta: { title: "院系管理", roles: ["admin"], icon: "dept" },
            component: () => import("@/views/settings/department/index.vue"),
          },
          {
            path: "/major",
            name: "Major",
            meta: { title: "专业管理", roles: ["admin"], icon: "major" },
            component: () => import("@/views/settings/major/index.vue"),
          },
          {
            path: "/teacher",
            name: "Teacher",
            meta: { title: "教师管理", roles: ["admin"], icon: "tutor" },
            component: () => import("@/views/settings/teacher/index.vue"),
          },
          {
            path: "/student",
            name: "Student",
            meta: { title: "学生管理", roles: ["admin"], icon: "stu" },
            component: () => import("@/views/settings/student/index.vue"),
          },
          {
            path: "/course",
            name: "Course",
            meta: { title: "课程管理", roles: ["admin", "teacher", "student"], icon: "intro" },
            component: () => import("@/views/settings/course/index.vue"),
          },
          {
            path: "/elective",
            name: "Elective",
            meta: { title: "选课管理", roles: ["admin"], icon: "sc" },
            component: () => import("@/views/settings/elective/index.vue"),
          },
          {
            path: "/taught",
            name: "Taught",
            meta: { title: "讲授管理", roles: ["admin"], icon: "taught" },
            component: () => import("@/views/settings/taught/index.vue"),
          },
          {
            path: "/myTaught",
            name: "MyTaught",
            meta: { title: "我的讲授", roles: ["teacher"], icon: "taught" },
            component: () => import("@/views/settings/myTaught/index.vue"),
          },
          {
            path: "/myElective",
            name: "MyElective",
            meta: { title: "我的课程", roles: ["student"], icon: "sc" },
            component: () => import("@/views/settings/myElective/index.vue"),
          },
        ],
      },
      {
        path: "/messages",
        name: "Messages",
        meta: { title: "消息中心", icon: "msg", roles: ["admin", "teacher", "student"] },
        component: () => import("@/views/messages/index.vue"),
      },
      {
        path: "/user",
        name: "User",
        meta: { title: "个人中心", icon: "user", roles: ["admin", "teacher", "student"] },
        component: () => import("@/views/user/index.vue"),
      },
    ],
  },
  {
    path: "/403",
    name: "403",
    meta: { title: "没有权限" },
    component: () => import("@/views/error/403/index.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "404",
    meta: { title: "找不到页面" },
    component: () => import("@/views/error/404/index.vue"),
  },
  // {
  //   path: '/:pathMatch(.*)',
  //   redirect: '/404'
  // }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

// 全局路由守卫(前置)
router.beforeEach((to, from, next) => {
  // VNode.component?.exposed?.startLoading();
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

// 全局路由守卫(后置）
router.afterEach((to, from) => {
  // VNode.component?.exposed?.stopLoading();
});

export default router;
