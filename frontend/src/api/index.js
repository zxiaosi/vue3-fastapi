import request from '../utils/request';

export const fetchData = query => {
    return request({
        url: 'http://localhost:3000/table.json',
        method: 'get',
        params: query
    });
};

// 用户测试数据
export const userData = query => {
    return request({
        url: './users/?skip=0&limit=100',
        method: 'get',
        params: query
    });
};

// 根据id删除用户
export const delele_User = user_id => {
    return request({
        url: `./users/${user_id}`,
        method: 'delete'
    });
};

// 根据id修改用户
export const update_User = (user_id, data) => {
    return request({
        url: `./users/${user_id}`,
        method: 'put',
        data: data
    });
};

// 添加用户信息
export const add_User = (data) => {
    return request({
        url: `./users/`,
        method: 'post',
        data: data
    });
};