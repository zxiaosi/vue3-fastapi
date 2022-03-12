export interface messageType {
  date: string;
  title: string;
}

export interface stateType {
  [key: string]: messageType[];
}
