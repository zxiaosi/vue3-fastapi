import request from '../utils/request';

/**
 * 获取教师信息
 * @param {*} pageIndex 1
 * @param {*} pageSize 10
 * @returns 所有专业信息
 */
function read_datas(data) {
  return request({
    url: './teacher/',
    method: 'get',
    params: data
  });
};

/**
 * 获取教师信息
 * @param {*} id 
 * @returns 某个教师的信息
 */
function read_data(id) {
  return request({
    url: `./teacher/${id}`,
    method: 'get',
  });
};

/**
 * 添加教师信息
 * @param {*} data 教师对象
 * @returns 添加的教师对象
 */
function create_data(data) {
  return request({
    url: `./teacher/`,
    method: 'post',
    data: data
  });
};

/**
 * 根据id修改教师信息
 * @param {*} id 
 * @param {*} data 教师对象
 * @returns 修改的教师对象
 */
function update_data(id, data) {
  return request({
    url: `./teacher/${id}`,
    method: 'put',
    data: data
  });
};

/**
 * 根据id删除教师信息
 * @param {*} id 教师id
 * @returns 删除的教师信息
 */
function delete_data(id) {
  return request({
    url: `./teacher/${id}`,
    method: 'delete'
  });
};

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
} 