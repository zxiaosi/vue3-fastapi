import { defineStore } from "pinia";
import type { UserInfo } from "@/types";

interface Tags {
  name: string;
  path: string;
  title: string;
}

export const useStore = defineStore({
  id: "index",
  state: () => ({
    tagsList: [] as Tags[], // 标签列表
    collapse: false as boolean, // 侧边栏是否折叠
    userInfo: {} as UserInfo, // 用户信息
    messages: 4 as number, // 消息数量
  }),
  getters: {
    tagNameList(state) {
      return state.tagsList.map((item: Tags) => {
        return item.name;
      });
    },
  },
  actions: {
    /**
     * 根据索引删除标签
     * @param index 索引值
     */
    delTagsItem(index: number) {
      this.tagsList.splice(index, 1);
    },

    /**
     * 添加路由对象
     * @param route 路由对象
     */
    setTagsItem(route: Tags) {
      this.tagsList.push(route);
    },

    /**
     * 关闭全部标签
     */
    clearTags() {
      this.tagsList = [];
    },

    /**
     * 关闭其他标签
     * @param data 标签数组
     */
    closeTagsOther(data: Tags[]) {
      this.tagsList = data;
    },
  },
});
