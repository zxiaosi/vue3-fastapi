import request from '../utils/request';

/**
 * 获取学生信息
 * @param {*} pageIndex 1
 * @param {*} pageSize 10
 * @returns 所有学生信息
 */
function read_datas(pageIndex = 1, pageSize = 10) {
  return request({
    url: './student/',
    method: 'get',
    params: { pageIndex: pageIndex, pageSize: pageSize }
  });
};

/**
 * 获取学生信息
 * @param {*} id 
 * @returns 某个学生的信息
 */
function read_data(id) {
  return request({
    url: `./student/${id}`,
    method: 'get',
  });
};

/**
 * 添加学生信息
 * @param {*} data 学生对象
 * @returns 添加的学生对象
 */
function create_data(data) {
  return request({
    url: `./student/`,
    method: 'post',
    data: data
  });
};

/**
 * 根据id修改学生信息
 * @param {*} id 
 * @param {*} data 学生对象
 * @returns 修改的学生对象
 */
function update_data(id, data) {
  return request({
    url: `./student/${id}`,
    method: 'put',
    data: data
  });
};

/**
 * 根据id删除学生信息
 * @param {*} id 学生id
 * @returns 删除的学生信息
 */
function delete_data(id) {
  return request({
    url: `./student/${id}`,
    method: 'delete'
  });
};

/**
 * 获取关系字段
 * @returns 
 */
function student_relation() {
  return request({
    url: `./student/relation/`,
    method: 'get'
  });
}


export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  student_relation
} 