/**
 * 全局标题
 * @type {string}
 */
export const TITLE: string = "Demo";

/**
 * 是否是开发环境
 */
export const IS_DEV: boolean = true;

/**
 * 开发、测试、线上环境
 */
export const DEVELOPMENT: string = "http://127.0.0.1:8000"; // 开发环境
export const PRODUCTION: string = "http://150.158.87.218"; // 线上环境
export const BASE_URL: string = IS_DEV ? DEVELOPMENT : PRODUCTION;

/**
 * API地址
 */
export const API_URL: string = BASE_URL + "/api";

/**
 * TODO: Icon地址前缀(临时)
 */
export const ICON_URL: string = "https://i.imgtg.com/2023/02/27/";
// export const ICON_URL: string = BASE_URL + "/static/icon/";

/**
 * 用户头像地址前缀
 */
export const IMAGE_URL: string = BASE_URL + "/static/avatar/";

/**
 * 公钥
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
 */
export const LayoutPage: string = "Layout";