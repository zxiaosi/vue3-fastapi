import request from '../utils/request';

/**
 * 获取学生信息
 * @param {*} query 
 * @returns 所有学生信息
 */
export const read_students = query => {
    return request({
        url: './student/?skip=0&limit=100',
        method: 'get',
        params: query
    });
};

/**
 * 添加学生信息
 * @param {*} data 学生对象
 * @returns 添加的学生对象
 */
export const create_student = (data) => {
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
export const update_student = (student_id, data) => {
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
export const delete_student = student_id => {
    return request({
        url: `./student/${student_id}`,
        method: 'delete'
    });
};