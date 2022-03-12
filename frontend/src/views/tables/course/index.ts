import type { courseFormType } from "@/types/table";

export interface stateType {
  courseData: courseFormType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
