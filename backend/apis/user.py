#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/30 10:48
# @Author : zxiaosi
# @desc : 用户接口
from fastapi import APIRouter
from starlette.responses import Response

from common.depends import GetDB, CheckCookie, PageQuery
from common.result import ResultSchema, Result
from common.route_log import LogRoute
from core.security import rsa_decrypt_password, verify_password
from crud import resource_crud, user_crud, role_crud
from models import LocalUser
from schemas import MenuOut, UserOut, UserLogin
from common.custom_exc import UserErrors
from utils.handle_cookie import clear_cookie, set_cookie
from utils.handle_menu import generate_tree_menu

router = APIRouter(route_class=LogRoute)


@router.post("/login")
async def user_login(user: UserLogin, response: Response, db: GetDB) -> ResultSchema[UserOut]:
    """ 登录 """
    try:
        user_schema = user_crud.get_user_by_name(db, user.name)  # 获取用户信息
        if user_schema:
            password = rsa_decrypt_password(user.password)  # 解密密码 (已在方法内抛出 Error)
            assert verify_password(password, user_schema.password)  # 验证密码是否正确 (AssertionError)
        else:
            raise UserErrors(err_desc="用户不存在")
    except AssertionError:
        raise UserErrors(err_desc="用户名或密码错误")

    user_resource_obj = resource_crud.get_resource_by_user_id(db, user_schema.id)
    user_schema.permission_codes = [resource.permission_code for resource in user_resource_obj]  # 更新用户权限

    set_cookie(user.name, user_schema, response)  # 设置 Cookie
    return Result.success(data=UserOut.from_orm(user_schema))


@router.post("/signup")
async def user_signup(user: UserLogin, response: Response, db: GetDB) -> ResultSchema[UserOut]:
    """ 注册 """
    user_schema = user_crud.get_user_by_name(db, user.name)  # 获取用户信息
    if user_schema:
        raise UserErrors(err_desc="用户已存在")
    else:
        user.password = rsa_decrypt_password(user.password)  # 解密密码 (已在方法内抛出 Error)
        user_obj = user_crud.create(db, user)  # 创建用户
        user_schema = LocalUser.from_orm(user_obj)  # 将用户信息转换为 LocalUser
        role_obj = role_crud.get_role_by_code(db, "ROLE_GUEST")  # 获取游客角色
        user_schema.role_name = role_obj.name  # 设置用户角色名(游客不插入数据)

        set_cookie(user.name, user_schema, response)  # 设置 Cookie
        return Result.success(data=UserOut.from_orm(user_schema))


@router.post("/logout")
async def user_logout(response: Response, _user: CheckCookie) -> ResultSchema:
    """ 退出登录 """
    LocalUser.delete(_user.pk)  # 删除redis中的用户信息
    clear_cookie(response)  # 清除cookie
    return Result.success()


@router.get("/menu")
def user_menu(db: GetDB, _user: CheckCookie) -> ResultSchema[list[MenuOut]]:
    """ 获取用户菜单 """
    role_obj = role_crud.get_role_by_user_id(db, _user.id)
    if role_obj:
        resource_obj = resource_crud.get_resource_by_role_id(db, role_obj.id)
    else:
        resource_obj = resource_crud.get_resource_by_role_code(db, "ROLE_GUEST")
    menu = generate_tree_menu(resource_obj)
    return Result.success(data=menu)


# @router.get("/list", dependencies=[Depends(check_permission(["sys:user:list"]))])
@router.get("/list")
def users(db: GetDB, page: PageQuery, name: str | None = None) -> ResultSchema[list[UserOut]]:
    """ 获取用户列表 """
    users_obj = user_crud.get_all(db=db, page=page, name=name)
    total = user_crud.get_count(db)
    return Result.success(data=users_obj, total=total)
