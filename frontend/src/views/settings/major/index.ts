import type { DeptForm, MajorForm } from "@/types/table";

export interface State {
  majorData: MajorForm[];
  deptData: DeptForm[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
