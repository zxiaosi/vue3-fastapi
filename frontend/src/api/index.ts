import { get, post, put, del } from "@/request";
import type { tableDataListType, tableObjectType, tableDataType, delDataListType, todoType } from "./model";

/**
 * 测试权限接口
 */
export const check_redis = (): Promise<any> => get("/health-check");

/**
 * 退出登录
 */
export const logout = (): Promise<any> => post("/logout");

/**
 * 获取用户信息
 */
export const get_current_user = (): Promise<any> => get("/dashboard/userInfo");

/**
 * 获取首页数据(语言详情 && 待办事项)
 */
export const get_lang_todo_list = (): Promise<any> => get("/dashboard/lang_todo_list");

/**
 * 查询首页数据(访问量 && 待办事项 && 请求数)
 */
export const get_visit_todo_request = (): Promise<any> => get("/dashboard/visit_todo_request");

/**
 * 添加待办
 */
export const add_todo = (data: todoType): Promise<any> => post(`/todo/add`, { ...data });

/**
 * 根据索引更新待办
 */
export const update_todo = (data: todoType): Promise<any> => post(`/todo/update`, { ...data });

/**
 * 获取表的数据
 */
export const read_datas = (data: tableDataListType): Promise<any> => {
  let { path, ...rest } = data;
  return get(`${path}/`, { ...rest });
};

/**
 * 根据 id 查询信息
 */
export const read_data = (data: tableDataType): any => get(`${data.path}/${data.id}`);

/**
 * 添加表格信息
 */
export const create_data = (data: tableObjectType): Promise<any> => {
  let { path, ...rest } = data;
  return post(`${path}/`, { ...rest });
};

/**
 * 更新表格信息
 */
export const update_data = (data: tableObjectType): Promise<any> => {
  let { path, id, ...rest } = data;
  return put(`${path}/${id}`, { ...rest });
};

/**
 * 根据 id 删除表格信息
 * @param {*} id id
 */
export const delete_data = (data: tableDataType): Promise<any> => del(`${data.path}/${data.id}`);

/**
 * 同时删除多个表格信息
 * @param {*} idList id列表
 */
export const delete_datas = (data: delDataListType): Promise<any> => post(`${data.path}/del/`, data.idList);

/**
 * 只获取关系字段
 */
export const read_datas_relation = (path: string): Promise<any> => get(`${path}/relation/`);
