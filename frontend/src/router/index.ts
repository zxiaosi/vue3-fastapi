import { getMenus } from "@/apis";
import { LayoutPage, TITLE } from "@/assets/js/global";
import { getLocal, setLocal } from "@/request/auth";
import { useUserStore } from "@/stores";
import { ElMessage } from "element-plus";
import { createRouter, createWebHistory, type NavigationGuardNext, type RouteLocationNormalized } from "vue-router";

const routes = [
  { path: "/", redirect: "/dashboard" }, // 重定向
  {
    path: "/login",
    meta: { title: "登录" },
    component: () => import("@/views/Login.vue"),
  },
  {
    path: "/",
    name: LayoutPage, // 路由名称, 用于添加动态路由 (详见: https://router.vuejs.org/zh/guide/advanced/dynamic-routing.html#%E6%B7%BB%E5%8A%A0%E5%B5%8C%E5%A5%97%E8%B7%AF%E7%94%B1)
    component: () => import(`@/views/${LayoutPage}.vue`),
  },
  {
    path: "/:pathMatch(.*)*",
    meta: { title: "404" },
    component: () => import("@/views/404.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeResolve(async (to) => {
  const userStore = useUserStore();

  if (to.path !== "/login" && userStore.menu.length == 0) { // 检查是否存在菜单列表, 不存在则获取菜单列表 (避免无限重定向)
    const menus = getLocal("menus");
    if (menus) {
      userStore.addRoutes(menus, router); // 添加动态路由
      return { ...to, replace: true };
    } else {
      try {
        const { data: { data } } = await getMenus(); // 获取菜单列表
        if (data.length > 0) {
          userStore.addRoutes(data, router); // 添加动态路由
          return { ...to, replace: true };
        } else {
          ElMessage.error("菜单列表为空");
          return false;
        }
      } catch (error: any) {
        throw error; // 抛出异常, 被全局异常捕获
      }
    }
  }
});

router.beforeEach((to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {
  document.title = `${to.meta.title} | ${TITLE}`; // 页面名

  if (to.path !== "/login" && !document.cookie) { // 检查是否存在cookie, 不存在则用户登录状态失效 (避免无限重定向)
    ElMessage.error("登录状态失效, 请重新登录");
    next("/login"); // 重定向到登录页
  } else {
    next();
  }
});

export default router;
