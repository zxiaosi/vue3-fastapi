import axios, { AxiosError } from "axios";
import type { AxiosRequestConfig, AxiosResponse } from "axios";
import { ElMessage } from "element-plus";
import { API_URL_DEVELOPMENT, API_URL_PRODUCTION } from "@/assets/js/global";
import { clearLocal } from "./auth";

/**
 * 错误处理: https://www.axios-http.cn/docs/handling_errors
 * ① 发送请求时出了点问题，比如网络错误
 * ② 请求已经成功发起，但没有收到响应
 * ③ 请求成功发出且服务器也响应了状态码，但状态代码超出了 2xx 的范围
 */

// 是否是开发环境
const isDev: boolean = true;

// Axios全局配置 https://axios-http.com/docs/config_defaults
axios.defaults.baseURL = isDev ? API_URL_DEVELOPMENT : API_URL_PRODUCTION;

// 请求拦截器(全局配置)
axios.interceptors.request.use(
  (config: any) => {
    config.withCredentials = true; // 跨域请求时携带Cookie
    config.headers = { "Content-Type": "application/json;charset=utf-8" }; // 请求头
    return config;
  },
  (error: AxiosError) => { // 发送请求时出了点问题，比如网络错误 https://segmentfault.com/q/1010000020659252
    ElMessage.error(`请求发起错误 -- ${error.message}`);
    return Promise.reject(error);
  }
);

// 响应拦截器(全局配置)
axios.interceptors.response.use(
  (response: AxiosResponse) => { // status >= 200 && status < 300 (HTTP 成功)
    const { data: { code, msg }, config } = response;
    const { isShowLoading, isShowFailToast, isThrowError } = config as IRequestOption; // 请求配置
    
    if (code == 0) { // 业务成功 (后端定义的成功)
      if (isShowLoading) ElMessage.success("请求成功！");
    } else { // 业务失败 (后端定义的失败)
      if (isShowLoading || isShowFailToast) ElMessage.error(msg);
      if (isThrowError) throw new Error(`后端返回的错误信息-- ${msg}`); // 抛出错误, 阻止程序向下执行 (默认配置)
    }

    return response;
  },
  (error: AxiosError) => { // HTTP 失败
    const { response, config } = error;
    const { url, isShowLoading, isShowFailToast, isThrowError } = config as IRequestOption;
    
    let errMsg = ""; // 错误信息

    if (response) { // 请求成功发出且服务器也响应了状态码，但状态代码超出了 2xx 的范围
      const { status, data } = response as AxiosResponse;
      errMsg = data.msg || `url:${(url || "").toString()},statusCode:${status}`;

      if (status == 401) {// 跳转登录
        setTimeout(() => { window.location.href = "/login" }, 2000);
        clearLocal();
      }
    } else { // 请求已经成功发起，但没有收到响应
      errMsg = "请求超时或服务器异常，请检查网络或联系管理员！";
    }

    if (isShowLoading || isShowFailToast) ElMessage.error(errMsg);

    return Promise.reject(isThrowError ? new Error(`请求失败 -- ${errMsg}`) : error);
  }
);

/** 自定义请求体 */
export interface IRequestData {
  [key: string]: any;
}

/** 自定义响应体 */
export interface IResponseData<T> {
  code: number;
  msg: string;
  data: T;
  total?: number;
}

/** 自定义配置项 */
export interface IRequestOption extends Partial<AxiosRequestConfig<string | IRequestData>> {
  /**
   * 是否显示Loading遮罩层
   * @default false
   */
  isShowLoading?: boolean;

  /**
   * 是否显示失败Toast弹框
   * @default true
   */
  isShowFailToast?: boolean;

  /**
   * 是否抛出错误 (阻止代码的继续运行)
   * @default true
   */
  isThrowError?: boolean;
}

// 封装请求类
class Http {
  defaultOptions: IRequestOption = {
    // 自定义配置项默认值
    isShowLoading: false,
    isShowFailToast: true,
    isThrowError: true,
  };

  // 请求配置 https://www.axios-http.cn/docs/req_config
  request<T>(url: string, data: string | object = {}, options: IRequestOption): Promise<AxiosResponse<string | IResponseData<T>>> {
    const requestUrl = url;
    const requestData = this.transformParam(options, data);
    const requestOptions = { ...this.defaultOptions, ...options };
    const config = { url: requestUrl, data: requestData, ...requestOptions };

    return axios.request(config);
  }

  /** 处理请求参数 */
  transformParam(options: IRequestOption, param: any) {
    if (options.method == "GET" || options.method == "DELETE") {
      let paramStr = "";
      for (const i in param) {
        // 防止特殊字符
        if (paramStr === "") paramStr += "?" + i + "=" + encodeURIComponent(param[i]);
        else paramStr += "&" + i + "=" + encodeURIComponent(param[i]);
      }
      return paramStr;
    } else {
      return param;
    }
  }
}

const http = new Http();
export default http;
