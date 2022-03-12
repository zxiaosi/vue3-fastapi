import type { deptFormType, majorFormType } from "@/types/table";

export interface stateType {
  majorData: majorFormType[];
  deptData: deptFormType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
