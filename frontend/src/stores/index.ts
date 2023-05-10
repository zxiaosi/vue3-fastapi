import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { iterateMenu } from "@/utils/handle_data";
import { LayoutPage } from "@/assets/js/global";
import { getLocal, setLocal } from "@/request/auth";

export const useUserStore = defineStore("userStore", () => {
  const user = ref<any>(getLocal("userInfo") || {}); // 用户信息
  const menu = ref<any>([]); // 菜单列表

  // const doubleCount = computed(() => count.value * 2)

  /**
   * 添加动态路由，并同步到状态管理器中
   * @param data 路由列表
   * @param router 路由实例
   */
  const addRoutes = (data: any, router: any) => {
    setLocal("menus", data);
    menu.value = iterateMenu(data);
    menu.value.forEach((item: any) => router.addRoute(LayoutPage, item));

    /**
     * router.getRoutes() 获取的是所有路由，扁平化输出，看不到嵌套的路由，但实际有嵌套的路由
     * 详见: https://github.com/vuejs/router/issues/600
     */
    // console.log("router", router.getRoutes());
  }

  const updateUser = (data: any) => {
    user.value = { ...user.value, ...data };
  }

  return { user, menu, addRoutes, updateUser };
});
