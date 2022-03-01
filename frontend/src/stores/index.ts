import { defineStore } from "pinia";

interface tagType {
  name: string;
  title: string;
  path: string;
}

interface stateType {
  tagsList: tagType[];
  collapse: boolean;
}

export const useStore = defineStore({
  id: "index",
  state: (): stateType => ({
    tagsList: [], // 标签列表
    collapse: false, // 侧边栏是否折叠
  }),
  getters: {},
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
