import http from "./http";
import type { IRequestData, IRequestOption } from "./http";

export function get<T = any>(url: string, data?: string | IRequestData, option: IRequestOption = {}) {
  return http.request<T>(url, data, { method: "GET", ...option });
}

export function post<T = any>(url: string, data?: string | IRequestData, option: IRequestOption = {}) {
  return http.request<T>(url, data, { method: "POST", ...option });
}

export function put<T = any>(url: string, data?: string | IRequestData, option: IRequestOption = {}) {
  return http.request<T>(url, data, { method: "PUT", ...option });
}

export function del<T = any>(url: string, data?: string | IRequestData, option: IRequestOption = {}) {
  return http.request<T>(url, data, { method: "DELETE", ...option });
}
export default http;
