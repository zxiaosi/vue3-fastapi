import request from '../utils/request';

/**
 * 获取院系信息 
 * @param {*} id 
 * @returns 所有院系信息 || 某个院系信息
 */
function read_datas(id) {
    return request({
        url: `./department/?skip=0&limit=100`,
        method: 'get',
        params: { departments_id: id }
    });
};

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
 * @param {*} department_id 
 * @param {*} data 院系对象
 * @returns 修改的院系对象
 */
function update_data(department_id, data) {
    return request({
        url: `./department/${department_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除院系信息
 * @param {*} department_id 院系id
 * @returns 删除的院系信息
 */
function delete_data(department_id) {
    return request({
        url: `./department/${department_id}`,
        method: 'delete'
    });
};

export default {
    read_datas,
    create_data,
    update_data,
    delete_data
} 