export interface Language {
  title: string;
  percentage: number;
  color: string;
}

export interface Todo {
  title: string;
  status: boolean;
}

export interface State {
  identity: string;
  langDetails: Language[];
  todoList: Todo[];
  visitNum: number;
  todoNum: number;
  requestNum: number;
  showDialog: boolean;
  todoText: string;
}

export enum RolesEnum {
  "admin" = "管理员",
  "teacher" = "教师",
  "student" = "学生",
}
