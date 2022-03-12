import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from "axios";
import { ElLoading, ElMessage } from "element-plus";
import type { LoadingInstance } from "element-plus/lib/components/loading/src/loading";
import type { ResponseData } from "@/types";
import { showStatus } from "./statusCode";
import { API_URL, TIME_OUT } from "@/assets/global";
import { getLocal } from "./auth";

// 请求
class AppRequest {
  instance: AxiosInstance; // axios实例
  loading?: LoadingInstance; // 加载动画

  // 构造器
  constructor(config: AxiosRequestConfig) {
    this.instance = axios.create(config);
  }

  /**
   * 自定义请求
   */
  request<T>(config: AxiosRequestConfig): Promise<ResponseData<T>> {
    return new Promise((resolve, reject) => {
      this.instance
        .request<any, any>(config)
        .then((res) => resolve(res.data))
        .catch((err) => reject(err));
    });
  }

  /**
   * 开始加载动画: https://www.cxybb.com/article/weixin_45685252/114917309
   */
  startLoading() {
    this.closeLoading(); // 先清除动画, 防止连续请求两次

    this.loading = ElLoading.service({
      // target: ".el-table, .table-flex, .region", // 设置加载动画区域
      target: ".el-table, .ms-content", // 设置加载动画区域(样式class名)
      lock: true, // 锁定屏幕的滚动
      text: "正在请求数据...", // 文案
    });

    // 设定定时器，超时5S后自动关闭遮罩层，避免请求失败时，遮罩层一直存在的问题
    setTimeout(() => this.closeLoading(), 5000); // 关闭遮罩层
  }

  /**
   * 关闭加载动画
   */
  closeLoading() {
    this.loading?.close(); // 关闭遮罩层
  }
}

// 创建对象
const http = new AppRequest({
  baseURL: API_URL, // url链接
  timeout: TIME_OUT, // 超时时间
  headers: { "Content-Type": "application/json;charset=utf-8" }, // 请求头
  transformRequest: [
    // 请求参数序列化(对象转字符串)
    (data) => {
      return JSON.stringify(data);
    },
  ],
  validateStatus() {
    // 使用async-await，处理reject情况较为繁琐，所以全部返回resolve，在业务代码中处理异常
    return true;
  },
  transformResponse: [
    // 响应数据反序列化(字符串转对象)
    (data) => {
      if (typeof data === "string" && data.startsWith("{")) {
        data = JSON.parse(data);
      }
      return data;
    },
  ],
});

// 请求拦截器
http.instance.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    http.startLoading(); // 加载动画

    //获取token，并将其添加至请求头中
    let token = getLocal("Authorization");
    if (token) {
      // @ts-ignore
      config.headers.Authorization = "Bearer " + token; // 前面一定要加 Bearer
    }

    return config;
  },
  (error) => {
    // @ts-ignore
    error.data.msg = "服务器异常，请联系管理员！";
    return Promise.reject(error);
  }
);

// 响应拦截器
http.instance.interceptors.response.use(
  (response: AxiosResponse) => {
    http.closeLoading(); // 关闭加载动画

    let msg = "";
    if (response.status == 200 && typeof response.status == "number") {
      return response;
    } else if (response.status == 401) {
      // 后端验证是否有token,没有则返回401
      window.location.href = "/login"; // 跳转登录
      return false;
    } else {
      if (response.data.msg != null) {
        msg = response.data.msg; // 后端返回的msg
      } else {
        msg = showStatus(response.status); // 后端未返回msg,前端根据状态码自定义的msg
      }
      ElMessage.error(msg);
    }
  },
  (error) => {
    if (axios.isCancel(error)) {
      console.log("repeated request: " + error.message);
    } else {
      error.data = {};
      error.data.msg = "请求超时或服务器异常，请检查网络或联系管理员！";
      ElMessage.error(error.data.msg);
    }
    return Promise.reject(error);
  }
);

export default http;
