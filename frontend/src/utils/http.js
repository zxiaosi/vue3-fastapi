import request from './request'

const http = {
  /**
   * methods: 请求方式
   * url 请求地址 
   * params 请求参数
   */

  // get请求
  get(url, params) {
    const config = { method: 'get', url: url }
    if (params) config.params = params
    return request(config)
  },

  // post请求
  post(url, data) {
    const config = { method: 'post', url: url }
    if (data) config.data = data
    return request(config)
  },

  // put请求
  put(url, data) {
    const config = { method: 'put', url: url }
    if (data) config.data = data
    return request(config)
  },

  // delete请求
  delete(url, params) {
    const config = { method: 'delete', url: url }
    if (params) config.params = params
    return request(config)
  }
}

export default http