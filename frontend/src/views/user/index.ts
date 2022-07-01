export interface UserInfo {
  [key: string]: any;
}

export interface Details {
  text: string;
  value: any;
}

export interface State {
  role: string;
  foreignKeyName: string;
  details: Details[];
}

// 性别枚举
export enum SexEnum {
  "男",
  "女",
}

// 学历枚举
export enum EduEnum {
  "学士",
  "硕士",
  "博士",
}

// 职称枚举
export enum TitleEnum {
  "助教",
  "讲师",
  "副教授",
  "教授",
}
