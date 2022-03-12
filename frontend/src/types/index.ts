/**
 * 请求参数(前端发送的数据格式)
 */
export interface RequestData {
  [key: string]: any;
}

/**
 * 响应数据(后端返回字段)
 */
export interface ResponseData<T> {
  code: number; // 状态码
  msg: string; // 成功/报错信息
  data: T; // 数据
}

/**
 * 权限枚举(与后端统一)
 */
export enum PermissEnum {
  admin = "admin", // 管理员权限
  teacher = "teacher", // 教师权限
  student = "student", // 学生权限
}

/**
 * 缓存存储的字段
 */
export interface userInfoType {
  name: string; // 名称
  address: string; // 地址
  avatar: string; // 头像
  modifyTime: string; // 最后更新时间
}
