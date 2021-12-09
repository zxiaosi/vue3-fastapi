import request from '../utils/request';

/**
 * 获取选课信息
 * @param {*} id 选课id 
 * @returns 所有选课信息 || 某个选课信息
 */
function read_datas(id) {
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
function create_data(data) {
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
function update_data(select_course_id, data) {
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
function delete_data(select_course_id) {
    return request({
        url: `./selectCourse/${select_course_id}`,
        method: 'delete'
    });
};

export default {
    read_datas,
    create_data,
    update_data,
    delete_data
} 