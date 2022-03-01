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
