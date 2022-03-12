import type { PermissEnum } from "@/types";
import type { formDataType, pathEnum } from "@/types/table";

/**
 * 登录
 */
export interface loginType {
  username: string;
  password: string;
  scope: PermissEnum[];
}

/**
 * 添加待办/根据索引更新待办
 */
export interface todoType {
  id?: number; // 待办索引(临时数据)
  title?: string; // 待办文案
  status?: boolean; // 是否选中
}

/**
 * 获取所有数据
 */
export interface tableDataListType {
  path: pathEnum;
  pageIndex?: number; // 页码
  pageSize?: number; // 每页个数
}

/**
 * 根据id查询/删除(多条)信息
 */
export interface tableDataType {
  path: pathEnum;
  id: number | string; // id
}

/**
 * 添加/更新信息
 */
export interface tableObjectType extends formDataType {
  path: pathEnum;
}

/**
 * 同时删除多个信息
 */
export interface delDataListType {
  path: pathEnum;
  idList: number[] | string[]; // id列表
}
