import request from '../utils/request';

/**
 * 获取教师信息
 * @param {*} query 
 * @returns 所有教师信息
 */
export const read_teachers = query => {
    return request({
        url: './teacher/?skip=0&limit=100',
        method: 'get',
        params: query
    });
};

/**
 * 添加教师信息
 * @param {*} data 教师对象
 * @returns 添加的教师对象
 */
export const create_teacher = (data) => {
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
export const update_teacher = (teacher_id, data) => {
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
export const delete_teacher = teacher_id => {
    return request({
        url: `./teacher/${teacher_id}`,
        method: 'delete'
    });
};