import type { CourseForm } from "@/types/table";

export interface State {
  courseData: CourseForm[];
  pageTotal: number;
  isDisabled: boolean;
}
