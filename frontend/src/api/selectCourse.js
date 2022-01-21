import http from '@/utils/http';

let resquest = './selectCourse/'

/**
 * 所有选课信息(根据页码和每页个数)
 * @param {*} params { pageIndex:1, pageSize:10 }
 * @returns 所有选课信息
 */
function read_datas(params) { return http.get(`${resquest}`, params) }

/**
 * 根据 id 查询选课信息
 * @param {*} id 
 * @returns 某个选课信息
 */
function read_data(id) { return http.get(`${resquest}${id}`) }

/**
 * 添加选课信息
 * @param {*} data 选课对象
 * @returns 添加的选课对象
 */
function create_data(data) { return http.post(`${resquest}`, data) }

/**
 * 根据id修改选课信息
 * @param {*} id 编号
 * @param {*} data 选课对象
 * @returns 修改的选课对象
 */
function update_data(id, data) { return http.put(`${resquest}${id}`, data) }

/**
 * 根据id删除选课信息
 * @param {*} id 选课id
 * @returns 删除的选课信息
 */
function delete_data(id) { return http.delete(`${resquest}${id}`) }

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data
} 