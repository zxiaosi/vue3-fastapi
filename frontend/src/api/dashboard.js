import http from '@/utils/http';

/**
 * 获取首页数据
 * @returns 
 */
export const get_dashboard = () => { return http.get(`./dashboard`) }

/**
 * 添加待办
 * @param {*} todo 待办信息
 * @returns 
 */
export const add_todo = (todo) => { return http.post(`./add/todo?todo_in=${todo}`) }

/**
 * 勾选待办
 * @param {*} id 待办编号
 * @returns 
 */
export const update_todo = (id) => { return http.put(`./update/todo?id=${id}`) }
