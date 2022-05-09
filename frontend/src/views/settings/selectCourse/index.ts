import type { CourseForm, SelectCourseForm, StudentForm, TeacherForm } from "@/types/table";

export interface stateType {
  selectCourseData: SelectCourseForm[];
  studentData: StudentForm[];
  teacherData: TeacherForm[];
  courseData: CourseForm[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
}
