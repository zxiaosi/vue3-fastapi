#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 16:23
# @Author : zxiaosi
# @desc : 依赖项
from fastapi import Depends
from redis_om import NotFoundError
from starlette import status
from starlette.requests import Request

from core.config import settings
from core.init_db import Session
from models import LocalUser
from utils.custom_exc import BadCredentials, UserErrors


def get_db():
    """ 得到数据库的会话 """
    with Session() as session:  # 会话工厂(工厂对象帮助我们管理)
        yield session


def check_cookie(request: Request):
    """ 校验cookie -- 认证"""
    if request.get("path") in settings.COOKIE_NOT_CHECK:  # 不校验Cookie
        return

    session = request.cookies.get(settings.COOKIE_KEY)
    try:
        # print(LocalUser.get(session).json())
        return LocalUser.get(session)
    except NotFoundError:
        raise BadCredentials()


def check_permission(code: list[str] = None):
    """ 校验权限code -- 权限"""

    def wrapper(user: LocalUser = Depends(check_cookie)):
        # TODO 获取 JsonModel 里面的数据是真的麻烦 eg: resource.json()
        resources = [resource.permission_code for resource in user.resources]
        # 判断一个列表中是否包含另一个列表中的元素
        if not set(code).issubset(set(resources)):
            raise UserErrors(code=status.HTTP_403_FORBIDDEN, err_desc="没有权限")

    return wrapper
