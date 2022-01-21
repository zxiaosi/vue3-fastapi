import http from '@/utils/http';

let resquest = './course/'

/**
 * 所有学生信息(根据页码和每页个数)
 * @param {*} params { pageIndex:1, pageSize:10 }
 * @returns 所有学生信息
 */
function read_datas(params) { return http.get(`${resquest}`, params) }

/**
 * 根据 id 查询课程信息
 * @param {*} id 
 * @returns 课程信息
 */
function read_data(id) { return http.get(`${resquest}${id}`) }

/**
 * 添加课程信息
 * @param {*} data 课程对象
 * @returns 添加的课程对象
 */
function create_data(data) { return http.post(`${resquest}`, data) }

/**
 * 根据id修改课程信息
 * @param {*} id 课程号
 * @param {*} data 课程对象
 * @returns 修改的课程对象
 */
function update_data(id, data) { return http.put(`${resquest}${id}`, data) }

/**
 * 根据id删除课程信息
 * @param {*} id 课程号
 * @returns 删除的课程信息
 */
function delete_data(id) { return http.delete(`${resquest}${id}`) }

/**
 * 获取关系字段
 * @returns 所有关系字段数据
 */
function course_relation() { return http.get(`${resquest}relation/`) }

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  course_relation
} 