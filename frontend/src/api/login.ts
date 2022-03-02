import http from "@/request/http";
import { BASE_URL } from "@/assets/global";
import type { loginType } from "./model";

/**
 * 登录(发送表单请求)
 */
export const login = (data: loginType): Promise<any> =>
  http.request({
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    url: `${BASE_URL}/login`,
    method: "POST",
    data: data,
    transformRequest: [
      // 将{username:111,password:111} 转成 username=111&password=111
      function (data) {
        var ret = "";
        for (var it in data) {
          ret += encodeURIComponent(it) + "=" + encodeURIComponent(data[it]) + "&"; // 如果要发送中文 编码
        }
        return ret.substring(0, ret.length - 1);
      },
    ],
  });
