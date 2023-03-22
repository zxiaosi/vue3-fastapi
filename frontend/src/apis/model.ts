export interface Login {
  name: string;
  password: string;
}

export interface SignUp extends Login {
}

export interface List {
  page?: number;
  page_size?: number;
  order_by?: string;
  order?: string;
  [key: string]: any;
}