import request from '../utils/request';

/**
 * 获取院系信息
 * @param {*} query 
 * @returns 所有院系信息
 */
export const read_departments = query => {
    return request({
        url: './department/?skip=0&limit=100',
        method: 'get',
        params: query
    });
};

/**
 * 添加院系信息
 * @param {*} data 院系对象
 * @returns 添加的院系对象
 */
export const create_department = (data) => {
    return request({
        url: `./department/`,
        method: 'post',
        data: data
    });
};

/**
 * 根据id修改院系信息
 * @param {*} department_id 
 * @param {*} data 院系对象
 * @returns 修改的院系对象
 */
export const update_department = (department_id, data) => {
    return request({
        url: `./department/${department_id}`,
        method: 'put',
        data: data
    });
};

/**
 * 根据id删除院系信息
 * @param {*} department_id 院系id
 * @returns 删除的院系信息
 */
export const delete_department = department_id => {
    return request({
        url: `./department/${department_id}`,
        method: 'delete'
    });
};