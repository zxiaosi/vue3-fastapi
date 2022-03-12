import type { formDataType, relationData } from "@/types/table";

export interface stateType {
  pathParam: any;
  pageName: any;
  searched: formDataType[];
  isShowSearched: boolean;
  selectedList: string[];
  relationData: relationData[];
  showDialog: boolean;
  addOrUpdate: boolean;
}
