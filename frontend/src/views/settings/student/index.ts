import type { StudentForm, MajorForm } from "@/types/table";

export interface State {
  studentData: StudentForm[];
  majorData: MajorForm[];
  pageTotal: number;
  isDisabled: boolean;
  isShowSearched: boolean;
  addOrUpdate: boolean;
}

export enum SexEnum {
  "男",
  "女",
}

export enum TagEnum {
  "success",
  "danger",
}
