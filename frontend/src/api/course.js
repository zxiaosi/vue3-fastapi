import request from '../utils/request';

/**
 * 获取课程信息
 * @param {*} id 课程id 
 * @returns 所有课程信息 || 某个课程信息
 */
export const read_courses = (id) => {
    return request({
        url: './course/?skip=0&limit=100',
        method: 'get',
        params: { course_id: id }
    });
};

/**
 * 添加课程信息
 * @param {*} data 课程对象
 * @returns 添加的课程对象
 */
export const create_course = (data) => {
    return request({
        url: `./course/`,
        method: 'post',
        data: data
    });
};

/**
 * 根据id修改课程信息
 * @param {*} course_id 
 * @param {*} data 课程对象
 * @returns 修改的课程对象
 */
export const update_course = (course_id, data) => {
    return request({
        url: `./course/${course_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除课程信息
 * @param {*} course_id 课程id
 * @returns 删除的课程信息
 */
export const delete_course = course_id => {
    return request({
        url: `./course/${course_id}`,
        method: 'delete'
    });
};