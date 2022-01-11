import request from '../utils/request';

/**
 * 获取专业信息
 * @param {*} pageIndex 1
 * @param {*} pageSize 10
 * @returns 所有选课信息
 */
function read_datas(pageIndex = 1, pageSize = 10) {
  return request({
    url: './selectCourse/',
    method: 'get',
    params: { pageIndex: pageIndex, pageSize: pageSize }
  });
};

/**
 * 获取专业信息
 * @param {*} id 
 * @returns 某个选课信息
 */
function read_data(id) {
  return request({
    url: `./selectCourse/${id}`,
    method: 'get',
  });
};

/**
 * 添加选课信息
 * @param {*} data 选课对象
 * @returns 添加的选课对象
 */
function create_data(data) {
  return request({
    url: `./selectCourse/`,
    method: 'post',
    data: data
  });
};

/**
 * 根据id修改选课信息
 * @param {*} id 
 * @param {*} data 选课对象
 * @returns 修改的选课对象
 */
function update_data(id, data) {
  return request({
    url: `./selectCourse/${id}`,
    method: 'put',
    data: data
  });
};

/**
 * 根据id删除选课信息
 * @param {*} id 选课id
 * @returns 删除的选课信息
 */
function delete_data(id) {
  return request({
    url: `./selectCourse/${id}`,
    method: 'delete'
  });
};

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data
} 