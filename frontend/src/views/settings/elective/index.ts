import type { CourseForm, ElectiveForm, StudentForm } from "@/types/table";

export interface State {
  electiveData: ElectiveForm[];
  studentData: StudentForm[];
  courseData: CourseForm[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
