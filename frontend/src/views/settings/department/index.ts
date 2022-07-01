import type { DeptForm } from "@/types/table";

export interface State {
  deptData: DeptForm[];
  pageTotal: number;
  isDisabled: boolean;
}
