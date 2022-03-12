import type { stuFormType, majorFormType } from "@/types/table";

export interface stateType {
  studentData: stuFormType[];
  majorData: majorFormType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
  addOrUpdate: boolean;
}

/**
 * 自定义枚举(性别)
 */
export interface enumType {
  [key: string]: { name: string; tag: string };
}
