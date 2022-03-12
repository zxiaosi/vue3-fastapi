import type { deptFormType } from "@/types/table";

export interface stateType {
  deptData: deptFormType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
