#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/30 10:48
# @Author : zxiaosi
# @desc : 用户接口
from fastapi import APIRouter
from sqlalchemy.exc import NoResultFound
from starlette.responses import Response

from common import LogRoute, CheckCookie, ResultSchema, Result, GetDB, PageQuery
from core.security import rsa_decrypt_password, verify_password
from crud import resource_crud, user_crud, user_role_crud
from models import LocalUser
from schemas import MenuOut, UserOut, UserLogin, UserRoleIn
from utils.custom_exc import UserErrors
from utils.handle_cookie import clear_cookie, set_cookie
from utils.handle_object import generate_tree_menu

router = APIRouter(route_class=LogRoute)


@router.post("/login")
async def user_login(user: UserLogin, response: Response, db: GetDB) -> ResultSchema[UserOut]:
    """ 登录 """
    try:
        user_obj = user_crud.get_user_by_name(db, user.name)  # 获取用户信息 (NoResultFound)
        password = rsa_decrypt_password(user.password)  # 解密密码 (已在方法内抛出 Error)
        assert verify_password(password, user_obj.password)  # 验证密码是否正确 (AssertionError)
    except NoResultFound:
        raise UserErrors(err_desc="用户不存在")
    except AssertionError:
        raise UserErrors(err_desc="用户名或密码错误")

    set_cookie(user.name, user_obj, response)  # 设置 Cookie
    return Result.success(data=user_obj)


@router.post("/signup")
async def user_signup(user: UserLogin, response: Response, db: GetDB) -> ResultSchema[UserOut]:
    """ 注册 """
    try:
        user_obj = user_crud.get_user_by_name(db, user.name)  # 获取用户信息 (NoResultFound)
        if user_obj:
            raise UserErrors(err_desc="用户已存在")
    except NoResultFound:
        user.password = rsa_decrypt_password(user.password)  # 解密密码 (已在方法内抛出 Error)
        user_obj = user_crud.create(db, user)  # 创建用户
        user_role_crud.create(db, UserRoleIn(user_id=user_obj.id, role_id=3))  # 关联用户和角色

        set_cookie(user.name, user_obj, response)  # 设置 Cookie
        return Result.success(data=user_obj)


@router.post("/logout")
async def user_logout(response: Response, _user: CheckCookie) -> ResultSchema:
    """ 退出登录 """
    LocalUser.delete(_user.pk)  # 删除redis中的用户信息
    clear_cookie(response)  # 清除cookie
    return Result.success()


@router.get("/menu")
def user_menu(db: GetDB, _user: CheckCookie) -> ResultSchema[list[MenuOut]]:
    """ 获取用户菜单 """
    user_resource_obj = resource_crud.get_resource_by_user_id(db, _user.id)

    # 获取过期时间： https://github.com/redis/redis-om-python/pull/238
    _user.permission_codes = [resource.permission_code for resource in user_resource_obj]  # 更新用户资源
    expire_time = LocalUser.db().ttl(_user.key())  # 获取过期时间(单独获取, 防止获取不到)
    _user.save().expire(expire_time)  # 更新用户资源

    menu = generate_tree_menu(user_resource_obj)
    return Result.success(data=menu)


# @router.get("/list", dependencies=[Depends(check_permission(["sys:user:list"]))])
@router.get("/list")
def users(db: GetDB, page: PageQuery, name: str | None = None) -> ResultSchema[list[UserOut]]:
    """ 获取用户列表 """
    users_obj = user_crud.get_all(db=db, page=page, name=name)
    total = user_crud.get_count(db)
    return Result.success(data=users_obj, total=total)
