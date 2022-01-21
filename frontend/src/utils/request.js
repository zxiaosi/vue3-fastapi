import axios from 'axios';
import { ElMessage } from 'element-plus';

const service = axios.create({
  baseURL: BASE_URL,
  timeout: TIMEOUT
});

service.interceptors.request.use(
  config => {
    // 请求拦截
    // if (localStorage.token) {
    //   config.headers.token = localStorage.token;
    // }
    return config;
  },
  error => {
    console.log("request--", error);
    return Promise.reject(error);
  }
);

service.interceptors.response.use(
  response => {
    if (response.status === 200 && typeof response.status == 'number') {
      return response.data;
    } else {
      console.log("request.js--response", response.data);
      Promise.reject();
    }
  },
  error => {
    if (error.response) {
      let data = error.response.data;
      if (data.code === 400) {
        ElMessage.error(data.msg);
      } else if (data.code === 401) {
        return Promise.reject(new Error('登录过期,请重新登录'));
      } else { // 请求被拒,或者链接写错
        console.log("request.js--error", data);
        ElMessage.error("未知错误！");
      }
      return Promise.reject(error.message);
    } else {
      // 连接不到服务器
      ElMessage.error("加载数据失败！");
      return Promise.reject(error);
    }
  }
);

export default service;
