import { defineStore } from "pinia";
import type { CourseForm, DeptForm, MajorForm, StudentForm, TeacherForm } from "@/types/table";

export const useDataStore = defineStore({
  id: "table",
  state: () => ({
    departmentData: [] as DeptForm[], // 院系
    majorData: [] as MajorForm[], // 专业
    teacherData: [] as TeacherForm[], // 教师
    studentData: [] as StudentForm[], // 学生
    courseData: [] as CourseForm[], // 课程
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
