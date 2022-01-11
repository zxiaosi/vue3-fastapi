import request from '../utils/request';

/**
 * 获取学生信息
 * @param {*} pageIndex 1
 * @param {*} pageSize 10
 * @returns 所有课程信息
 */
function read_datas(pageIndex = 1, pageSize = 10) {
  return request({
    url: './course/',
    method: 'get',
    params: { pageIndex: pageIndex, pageSize: pageSize }
  });
};

/**
 * 获取学生信息
 * @param {*} id 
 * @returns 某个课程信息
 */
function read_data(id) {
  return request({
    url: `./course/${id}`,
    method: 'get',
  });
};

/**
 * 添加课程信息
 * @param {*} data 课程对象
 * @returns 添加的课程对象
 */
function create_data(data) {
  return request({
    url: `./course/`,
    method: 'post',
    data: data
  });
};

/**
 * 根据id修改课程信息
 * @param {*} id 
 * @param {*} data 课程对象
 * @returns 修改的课程对象
 */
function update_data(id, data) {
  return request({
    url: `./course/${id}`,
    method: 'put',
    data: data
  });
};

/**
 * 根据id删除课程信息
 * @param {*} id 课程id
 * @returns 删除的课程信息
 */
function delete_data(id) {
  return request({
    url: `./course/${id}`,
    method: 'delete'
  });
};

/**
 * 获取关系字段
 * @returns 
 */
function course_relation() {
  return request({
    url: `./course/relation/`,
    method: 'get'
  });
}

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  course_relation
} 