import { defineStore } from "pinia";
import type { formDataType } from "@/types/table";

interface stateType {
  departmentData: formDataType[];
  majorData: formDataType[];
  teacherData: formDataType[];
  studentData: formDataType[];
  courseData: formDataType[];
}

export const useDataStore = defineStore({
  id: "data",
  state: (): stateType => ({
    departmentData: [], // 院系
    majorData: [], // 专业
    teacherData: [], // 教师
    studentData: [], // 学生
    courseData: [], // 课程
  }),
  getters: {},
  actions: {
    /**
     * 存储数据
     * @param prefix 表名
     * @param data 数据
     */
    handleData(prefix: string, data: string[]) {
      // console.log(prefix, data);
      this[`${prefix}Data`] = data;
    },
  },
});
