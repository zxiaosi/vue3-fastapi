import axios from "axios";
import { get, post, put, del } from "@/request";
import type { GetUserInfo, Todo, TableDataList, TableData, TableObject, DelDataList } from "./model";

/**
 * 退出登录
 */
export const logout = (): Promise<any> => post("/logout");

/**
 * 获取用户信息
 */
export const getUserInfo = (data: GetUserInfo): Promise<any> => get(`${data.roles}/index`);

/**
 * 查询首页数据(访问量 && 待办事项 && 请求数 && 待办事项)
 */
export const getDashboard = (): Promise<any> => get("/dashboard");

/**
 * 添加待办
 */
export const addTodo = (data: Todo): Promise<any> => post(`/todo/add`, { ...data });

/**
 * 根据索引更新待办
 */
export const updateTodo = (data: Todo): Promise<any> => post(`/todo/update`, { ...data });

/**
 * 获取表的数据
 */
export const readDatas = (data: TableDataList): Promise<any> => {
  const { path, ...rest } = data;
  return get(`${path}/`, { ...rest });
};

/**
 * 根据 id 查询信息
 */
export const readData = (data: TableData): Promise<any> => get(`${data.path}/${data.id}`);

/**
 * 添加表格信息
 */
export const createData = (data: TableObject): Promise<any> => {
  let { path, ...rest } = data;
  return post(`${path}/`, { ...rest });
};

/**
 * 更新表格信息
 */
export const updateData = (data: TableObject): Promise<any> => {
  let { path, id, ...rest } = data;
  return put(`${path}/${id}`, { ...rest });
};

/**
 * 根据 id 删除表格信息
 * @param {*} data id
 */
export const deleteData = (data: TableData): Promise<any> => del(`${data.path}/${data.id}`);

/**
 * 同时删除多个表格信息
 * @param {*} data id列表
 */
export const deleteDatas = (data: DelDataList): Promise<any> => post(`${data.path}/del/`, data.idList);

/**
 * 获取语言详情
 */
export const getLangList = async (): Promise<any> => {
  return await axios.get("https://api.github.com/repos/zxiaosi/Vue3-FastAPI/languages");
};
