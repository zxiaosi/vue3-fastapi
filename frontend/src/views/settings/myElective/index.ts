export interface Data {
  name?: string;
  grade: number;
  teacherName?: string;
  courseName: string;
  create_time: string;
}

export interface State {
  dataList: Data[];
}
