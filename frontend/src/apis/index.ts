import { get, post } from "@/request";
import type { IRequestOption } from "@/request/http";
import type { SignUp, Login, List } from "./model";

/** 注册 */
export const userSignUp = (data: SignUp): Promise<any> => post("/user/signup", { ...data });

/** 登录 */
export const userLogin = (data: Login): Promise<any> => post("/user/login", { ...data });

/** 登出 */
export const userLogout = (): Promise<any> => post("/user/logout");

/** 得到菜单 */
export const getMenus = (): Promise<any> => get("/user/menu");

/** 上传图片 */
export const uploadImg = (file: any, config: IRequestOption): Promise<any> => post("/upload/", file, { ...config });

/** 得到所有用户 */
export const getUsers = (list: List): Promise<any> => get("/user/list", { ...list });

/** 得到所有日志 */
export const getLogs = (list: List): Promise<any> => get("/log/list", { ...list });

/**
 * 仓库获取语言详情(github被封了, 暂时用不了)
 */
// export const getLangList = async (page: number): Promise<any> => {
//   return await axios.get(`https://api.github.com/repos/zxiaosi/Vue3-FastAPI/commits?page=${page}`);
// };

/** 仓库获取语言详情 */
export const getLangList = (): Promise<any> => get("/lang/list");