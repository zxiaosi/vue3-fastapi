import request from '../utils/request';

/**
 * 获取选课信息
 * @param {*} id 选课id 
 * @returns 所有选课信息 || 某个选课信息
 */
export const read_select_courses = (id) => {
    return request({
        url: './selectCourse/?skip=0&limit=100',
        method: 'get',
        params: { select_course_id: id }
    });
};

/**
 * 添加选课信息
 * @param {*} data 选课对象
 * @returns 添加的选课对象
 */
export const create_select_course = (data) => {
    return request({
        url: `./selectCourse/`,
        method: 'post',
        data: data
    });
};

/**
 * 根据id修改选课信息
 * @param {*} select_course_id 
 * @param {*} data 选课对象
 * @returns 修改的选课对象
 */
export const update_select_course = (select_course_id, data) => {
    return request({
        url: `./selectCourse/${select_course_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除选课信息
 * @param {*} select_course_id 选课id
 * @returns 删除的选课信息
 */
export const delete_select_course = (select_course_id) => {
    return request({
        url: `./selectCourse/${select_course_id}`,
        method: 'delete'
    });
};