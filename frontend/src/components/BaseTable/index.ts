import type { FormData } from "@/types/table";

export interface State {
  pageName: any;
  searched: FormData[];
  isShowSearched: boolean;
  selectedList: string[];
  relationData: any;
  showDialog: boolean;
  addOrUpdate: boolean;
  isStudent: boolean;
  isTeacher: boolean;
}
