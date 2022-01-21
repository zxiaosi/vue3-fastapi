import http from '@/utils/http';

let resquest = './major/'

/**
 * 所有专业信息(根据页码和每页个数)
 * @param {*} params { pageIndex:1, pageSize:10 }
 * @returns 所有专业信息
 */
function read_datas(params) { return http.get(`${resquest}`, params) }

/**
 * 根据 id 查询专业信息
 * @param {*} id 院系id
 * @returns 专业信息
 */
function read_data(id) { return http.get(`${resquest}${id}`) }

/**
 * 添加专业信息
 * @param {*} data 专业对象
 * @returns 添加的专业对象
 */
function create_data(data) { return http.post(`${resquest}`, data) }

/**
 * 根据id修改专业信息
 * @param {*} id 
 * @param {*} data 专业对象
 * @returns 修改的专业对象
 */
function update_data(id, data) { return http.put(`${resquest}${id}`, data) }

/**
 * 根据id删除专业信息
 * @param {*} id 专业id
 * @returns 删除的专业信息
 */
function delete_data(id) { return http.delete(`${resquest}${id}`) }

/**
 * 获取关系字段
 * @returns 所有关系字段数据
 */
function major_relation() { return http.get(`${resquest}relation/`) }

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  major_relation
} 