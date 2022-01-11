import request from '../utils/request';

/**
 * 获取院系信息 
 * @param {*} pageIndex 1
 * @param {*} pageSize 10
 * @returns 所有院系信息(根据页码和每页个数)
 */
function read_datas(pageIndex = 1, pageSize = 10) {
  return request({
    url: `./department/`,
    method: 'get',
    params: { pageIndex: pageIndex, pageSize: pageSize }
  });
};

/**
 * 根据 id 查询院系信息
 * @param {*} id 院系id
 * @returns 院系信息
 */
function read_data(id) {
  return request({
    url: `./department/${id}`,
    method: 'get'
  });
}

/**
 * 添加院系信息
 * @param {*} data 院系对象
 * @returns 添加的院系对象
 */
function create_data(data) {
  return request({
    url: `./department/`,
    method: 'post',
    data: data
  });
};

/**
 * 根据id修改院系信息
 * @param {*} id 院系id
 * @param {*} data 院系对象
 * @returns 修改的院系对象
 */
function update_data(id, data) {
  return request({
    url: `./department/${id}`,
    method: 'put',
    data: data
  });
};

/**
 * 根据id删除院系信息
 * @param {*} id 院系id
 * @returns 删除的院系信息
 */
function delete_data(id) {
  return request({
    url: `./department/${id}`,
    method: 'delete'
  });
};

/**
 * 获取关系字段
 * @returns 
 */
function department_relation() {
  return request({
    url: `./department/relation/`,
    method: 'get'
  });
}

export default {
  read_datas,
  read_data,
  create_data,
  update_data,
  delete_data,
  department_relation
} 