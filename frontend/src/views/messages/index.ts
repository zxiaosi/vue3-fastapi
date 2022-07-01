export interface Message {
  date: string;
  title: string;
}

export interface State {
  [key: string]: Message[];
}
