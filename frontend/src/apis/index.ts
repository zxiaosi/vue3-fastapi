import { get, post } from "@/request";
import type { SignUp, Login } from "./model";

/** 注册 */
export const userSignUp = (data: SignUp): Promise<any> => post("/user/signup", { ...data });

/** 登录 */
export const userLogin = (data: Login): Promise<any> => post("/user/login", { ...data });

/** 得到菜单 */
export const getMenus = (): Promise<any> => get("/user/menu");