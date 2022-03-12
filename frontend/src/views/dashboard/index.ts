import type { userInfoType } from "@/types";

export interface languageType {
  title: string;
  percentage: number;
  color: string;
}

export interface todoType {
  title: string;
  status: boolean;
}
export interface stateType {
  userInfo: userInfoType;
  languageDetails: languageType[];
  todoList: todoType[];
  visitNumber: number;
  todoNumber: number;
  requestNumber: number;
  showDialog: boolean;
  todoText: string;
}
