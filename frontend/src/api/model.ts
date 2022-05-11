import type { FormData, PathEnum } from "@/types/table";

/**
 * 登录
 */
export interface Login {
  username: string;
  password: string;
  scope: any;
}

/**
 * 获取用户信息
 */
export interface GetUserInfo {
  roles: "admin" | "student" | "teacher";
}

/**
 * 添加待办/根据索引更新待办
 */
export interface Todo {
  id?: number; // 待办索引(临时数据)
  title?: string; // 待办文案
  status?: boolean; // 是否选中
}

/**
 * 获取所有数据(表格数据)
 */
export interface TableDataList {
  path: PathEnum; // 路径参数
  pageIndex?: number; // 页码
  pageSize?: number; // 每页个数
}

/**
 * 根据id查询/删除(多条)信息
 */
export interface TableData {
  path: PathEnum; // 路径参数
  id: number | string; // id
}

/**
 * 添加/更新信息
 */
export interface TableObject extends FormData {
  path: PathEnum; // 路径参数
}

/**
 * 同时删除多个信息
 */
export interface DelDataList {
  path: PathEnum; // 路径参数
  idList: number[] | string[]; // id列表
}

/**
 * 根据课程id添加/删除选课信息
 */
export interface CourseId {
  path: PathEnum; // 路径参数
  courseId: number | string; // 课程id
}
/**
 * 得到课程详情
 */
export interface Details {
  path: PathEnum; // 路径参数
}
