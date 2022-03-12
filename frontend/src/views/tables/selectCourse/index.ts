import type { courseFormType, selectCourseFormType, stuFormType, teachFormType } from "@/types/table";

export interface stateType {
  selectCourseData: selectCourseFormType[];
  studentData: stuFormType[];
  teacherData: teachFormType[];
  courseData: courseFormType[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
