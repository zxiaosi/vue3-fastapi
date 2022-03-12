import { getLocal } from "@/request/auth";
import type { userInfoType } from "@/types";
import { defineStore } from "pinia";

interface tagType {
  name: string;
  title: string;
  path: string;
}

interface stateType {
  tagsList: tagType[];
  collapse: boolean;
  userInfo: userInfoType;
}

export const useStore = defineStore({
  id: "index",
  state: (): stateType => ({
    tagsList: [], // 标签列表
    collapse: false, // 侧边栏是否折叠
    userInfo: {
      name: "", // 用户名
      avatar: "", // 头像
      address: "", // 地址
      modifyTime: "", // 最后修改时间
    },
  }),
  getters: {
    tagNameList(state) {
      return state.tagsList.map((item) => {
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
    setTagsItem(route: tagType) {
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
    closeTagsOther(data: tagType[]) {
      this.tagsList = data;
    },
  },
});
