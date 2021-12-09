import request from '../utils/request';

/**
 * 获取学生信息
 * @param {*} id 学生id 
 * @returns 所有学生信息 || 某个学生的信息
 */
function read_datas(id) {
    return request({
        url: './student/?skip=0&limit=100',
        method: 'get',
        params: { student_id: id }
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
 * @param {*} student_id 
 * @param {*} data 学生对象
 * @returns 修改的学生对象
 */
function update_data(student_id, data) {
    return request({
        url: `./student/${student_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除学生信息
 * @param {*} student_id 学生id
 * @returns 删除的学生信息
 */
function delete_data(student_id) {
    return request({
        url: `./student/${student_id}`,
        method: 'delete'
    });
};

export default {
    read_datas,
    create_data,
    update_data,
    delete_data
} 