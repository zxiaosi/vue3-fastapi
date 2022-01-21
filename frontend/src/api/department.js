import http from '@/utils/http';

let resquest = './department/'

/**
 * 所有院系信息(根据页码和每页个数)
 * @param {*} params { pageIndex:1, pageSize:10 }
 * @returns 所有院系信息
 */
function read_datas(params) { return http.get(`${resquest}`, params) }


/**
 * 根据 id 查询院系信息
 * @param {*} id 院系id
 * @returns 院系信息
 */
function read_data(id) { return http.get(`${resquest}${id}`) }


/**
 * 添加院系信息
 * @param {*} data 院系对象
 * @returns 添加的院系对象
 */
function create_data(data) { return http.post(`${resquest}`, data) }

/**
 * 根据id修改院系信息
 * @param {*} id 院系id
 * @param {*} data 院系对象
 * @returns 修改的院系对象
 */
function update_data(id, data) { return http.put(`${resquest}${id}`, data) }

/**
 * 根据id删除院系信息
 * @param {*} id 院系id
 * @returns 删除的院系信息
 */
function delete_data(id) { return http.delete(`${resquest}${id}`) }

/**
 * 获取关系字段
 * @returns 所有关系字段数据
 */
function department_relation() { return http.get(`${resquest}relation/`) }

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  department_relation
} 