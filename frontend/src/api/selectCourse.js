import request from '../utils/request';

/**
 * 获取选课信息
 * @param {*} query 
 * @returns 所有选课信息
 */
export const read_select_courses = query => {
    return request({
        url: './selectCourse/?skip=0&limit=100',
        method: 'get',
        params: query
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
 * @param {*} selectCourse_id 
 * @param {*} data 选课对象
 * @returns 修改的选课对象
 */
export const update_select_course = (selectCourse_id, data) => {
    return request({
        url: `./selectCourse/${selectCourse_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除选课信息
 * @param {*} selectCourse_id 选课id
 * @returns 删除的选课信息
 */
export const delete_select_course = selectCourse_id => {
    return request({
        url: `./selectCourse/${selectCourse_id}`,
        method: 'delete'
    });
};