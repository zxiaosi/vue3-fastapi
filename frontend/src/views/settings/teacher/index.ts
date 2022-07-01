import type { DeptForm, TeacherForm } from "@/types/table";

export interface State {
  teacherData: TeacherForm[];
  deptData: DeptForm[];
  pageTotal: number;
  isDisabled: boolean;
  addOrUpdate: boolean;
}

export enum SexEnum {
  "男",
  "女",
}

export enum EduEnum {
  "学士",
  "硕士",
  "博士",
}

export enum TitleEnum {
  "助教",
  "讲师",
  "副教授",
  "教授",
}

export enum TagEnum {
  "",
  "success",
  "warning",
  "danger",
}
