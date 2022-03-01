import http from "./http";
import type { RequestData, ResponseData } from "@/types";

export function get<T>(url: string, data?: RequestData | string): Promise<ResponseData<T>> {
  return http.request<T>({ url, params: data, method: "GET" });
}

export function post<T>(url: string, data?: RequestData | string): Promise<ResponseData<T>> {
  return http.request<T>({ url, data: data, method: "POST" });
}

export function put<T>(url: string, data?: RequestData | string): Promise<ResponseData<T>> {
  return http.request<T>({ url, data: data, method: "PUT" });
}

export function del<T>(url: string, data?: RequestData | string): Promise<ResponseData<T>> {
  return http.request<T>({ url, params: data, method: "DELETE" });
}

export default http;
