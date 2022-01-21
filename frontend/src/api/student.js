import http from '@/utils/http';

let resquest = './student/'

/**
 * 所有学生信息(根据页码和每页个数)
 * @param {*} params { pageIndex:1, pageSize:10 }
 * @returns 所有学生信息
 */
function read_datas(params) { return http.get(`${resquest}`, params) }

/**
 * 根据 id 查询学生信息
 * @param {*} id 学号
 * @returns 学生的信息
 */
function read_data(id) { return http.get(`${resquest}${id}`) }
/**
 * 添加学生信息
 * @param {*} data 学生对象
 * @returns 添加的学生对象
 */
function create_data(data) { return http.post(`${resquest}`, data) }

/**
 * 根据id修改学生信息
 * @param {*} id 
 * @param {*} data 学生对象
 * @returns 修改的学生对象
 */
function update_data(id, data) { return http.put(`${resquest}${id}`, data) }

/**
 * 根据id删除学生信息
 * @param {*} id 学生id
 * @returns 删除的学生信息
 */
function delete_data(id) { return http.delete(`${resquest}${id}`) }

/**
 * 获取关系字段
 * @returns 所有关系字段数据
 */
function student_relation() { return http.get(`${resquest}relation/`) }


export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  student_relation
} 