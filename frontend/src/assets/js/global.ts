/**
 * 全局标题
 * @type {string}
 */
export const TITLE: string = "Demo";

/**
 * 环境
 * @type {string}
 */
export const API_URL_DEVELOPMENT: string = `http://127.0.0.1:8000/api`; // 开发环境
export const API_URL_PRODUCTION: string = `http://114.115.143.81/api`; // 线上环境

/**
 * TODO: 图片地址前缀(暂时)
 * @type {string}
 */
export const IMAGE_URL: string = "https://i.imgtg.com/2023/02/27/";

/**
 * 公钥
 * @type {string}
 */
export const PUBLIC_PEM: string = "\
-----BEGIN RSA PUBLIC KEY-----\
MIGJAoGBAIRZg26Mu59Yr9nPd5gjmAspPUD3hT0Z6MmDwGbqm49IjdboNyt69RBI\
UFGjqOGL7yE84pfbr48yL+7SxpJd9uDNFc7kO9zVOz+rgKBfn3kCDLyLrB7W6wH6\
DsajiPK45iVoHz8pzp+ELwOcLmiuHsFycSMep8FmfVZHhYxrzNqFAgMBAAE=\
-----END RSA PUBLIC KEY-----\
";

/**
 * 布局页面文件名称 eg: Layout
 * 修改布局文件步骤:
 *    1. 修改此处
 *    2. 修改 src\view\Layout.vue 文件名
 * @type {string}
 */
export const LayoutPage: string = "Layout";