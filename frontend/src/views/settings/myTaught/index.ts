export interface Data {
  name?: string;
  grade: number;
  studentName?: string;
  courseName: string;
  update_time: string;
}

export interface State {
  dataList: Data[];
  showDialog: boolean;
  electiveId: number;
}
