import request from '../utils/request';

/**
 * 获取专业信息
 * @param {*} query 
 * @returns 所有专业信息 || 某个专业信息
 */
function read_datas(id) {
    return request({
        url: './major/?skip=0&limit=100',
        method: 'get',
        params: { major_id: id }
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
 * @param {*} major_id 
 * @param {*} data 专业对象
 * @returns 修改的专业对象
 */
function update_data(major_id, data) {
    return request({
        url: `./major/${major_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除专业信息
 * @param {*} major_id 专业id
 * @returns 删除的专业信息
 */
function delete_data(major_id) {
    return request({
        url: `./major/${major_id}`,
        method: 'delete'
    });
};

export default {
    read_datas,
    create_data,
    update_data,
    delete_data
} 