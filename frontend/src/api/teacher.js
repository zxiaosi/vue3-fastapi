import request from '../utils/request';

/**
 * 获取教师信息
 * @param {*} id 教师id 
 * @returns 所有教师信息 || 某个教师的信息
 */
function read_datas(id) {
    return request({
        url: './teacher/?skip=0&limit=100',
        method: 'get',
        params: { teacher_id: id }
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
 * @param {*} teacher_id 
 * @param {*} data 教师对象
 * @returns 修改的教师对象
 */
function update_data(teacher_id, data) {
    return request({
        url: `./teacher/${teacher_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除教师信息
 * @param {*} teacher_id 教师id
 * @returns 删除的教师信息
 */
function delete_data(teacher_id) {
    return request({
        url: `./teacher/${teacher_id}`,
        method: 'delete'
    });
};

export default {
    read_datas,
    create_data,
    update_data,
    delete_data
} 