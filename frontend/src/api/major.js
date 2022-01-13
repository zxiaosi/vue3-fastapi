import request from '../utils/request';

/**
 * 获取专业信息
 * @param {*} pageIndex 1
 * @param {*} pageSize 10
 * @returns 所有专业信息
 */
function read_datas(data) {
  return request({
    url: './major/',
    method: 'get',
    params: data
  });
};

/**
 * 获取专业信息
 * @param {*} id 
 * @returns 某个专业信息
 */
function read_data(id) {
  return request({
    url: `./major/${id}`,
    method: 'get',
  });
};

/**
 * 添加专业信息
 * @param {*} data 专业对象
 * @returns 添加的专业对象
 */
function create_data(data) {
  return request({
    url: `./major/`,
    method: 'post',
    data: data
  });
};

/**
 * 根据id修改专业信息
 * @param {*} id 
 * @param {*} data 专业对象
 * @returns 修改的专业对象
 */
function update_data(id, data) {
  return request({
    url: `./major/${id}`,
    method: 'put',
    data: data
  });
};

/**
 * 根据id删除专业信息
 * @param {*} id 专业id
 * @returns 删除的专业信息
 */
function delete_data(id) {
  return request({
    url: `./major/${id}`,
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