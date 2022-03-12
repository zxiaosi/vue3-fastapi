import type { deptFormType, teachFormType } from "@/types/table";

export interface stateType {
  teacherData: teachFormType[];
  deptData: deptFormType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
  addOrUpdate: boolean;
}

/**
 * 自定义枚举(性别、学历、职称)
 */
export interface enumType {
  [key: string]: { name: string; tag: string };
}
