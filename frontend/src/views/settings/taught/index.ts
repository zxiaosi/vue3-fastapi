import type { TaughtForm, TeacherForm, CourseForm } from "@/types/table";

export interface State {
  taughtData: TaughtForm[];
  teacherData: TeacherForm[];
  courseData: CourseForm[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
