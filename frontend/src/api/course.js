import request from '../utils/request';

/**
 * 获取课程信息
 * @param {*} id 课程id 
 * @returns 所有课程信息 || 某个课程信息
 */
function read_datas(id) {
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
function create_data(data) {
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
function update_data(course_id, data) {
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
function delete_data(course_id) {
    return request({
        url: `./course/${course_id}`,
        method: 'delete'
    });
};

export default {
    read_datas,
    create_data,
    update_data,
    delete_data
} 