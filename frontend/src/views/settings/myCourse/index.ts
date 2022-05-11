export interface Data {
  name?: string;
  grade: number;
  teacher_name?: string;
  course_name: string;
  update_time: string;
}

export interface State {
  dataList: Data[];
}
