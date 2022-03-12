import http from "@/request/http";
import { API_URL } from "@/assets/global";
import type { loginType } from "./model";

/**
 * 登录(发送表单请求)
 */
export const login = (data: loginType): Promise<any> =>
  http.request({
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    url: `${API_URL}/login`,
    method: "POST",
    data: data,
    transformRequest: [
      // 请求时, 将{username:111,password:111} 转成 username=111&password=111
      function (data) {
        var ret = "";
        for (var it in data) {
          // 判断是否是数组
          if (Array.isArray(data[it])) {
            let tmp = data[it].join(" "); // 将 ['admin','teacher','student'] 中 , 转为 ' '
            ret += encodeURIComponent(it) + "=" + encodeURIComponent(tmp) + "&";
          } else {
            ret += encodeURIComponent(it) + "=" + encodeURIComponent(data[it]) + "&";
          }
        }
        return ret.substring(0, ret.length - 1);
      },
    ],
  });
