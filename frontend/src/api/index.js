import request from '../utils/request';

export const fetchData = query => {
    return request({
        url: './table.json',
        method: 'get',
        params: query
    });
};

// 用户测试数据
export const userData = () => {
    return request({
        url: './api/v1/users/?skip=0&limit=100',
        method: 'get'
    });
};

