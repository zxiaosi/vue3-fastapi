#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 16:23
# @Author : zxiaosi
# @desc : 依赖项
from typing import Annotated

from fastapi import Depends
from redis_om import NotFoundError
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request

from core.config import settings
from core.init_db import SessionLocal
from crud import resource_crud
from models import LocalUser
from utils.custom_exc import BadCredentials, UserErrors


def get_db():
    """ 得到数据库的会话 """
    db = SessionLocal()  # 会话工厂(工厂对象帮助我们管理)
    try:
        yield db
    finally:
        db.close()


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


def check_permission(code: list[str] | None = None):
    """ 校验权限code -- 权限"""

    def wrapper(request: Request, db: GetDB, user: CheckCookie):
        if not code:
            resource = resource_crud.get_resource_by_url(db, request.get("path").replace(settings.API_PREFIX, ""))
            if resource and resource.permission_code not in user.permission_codes:  # 查不到资源, 表示不需要权限
                raise UserErrors(code=status.HTTP_403_FORBIDDEN, err_desc="没有权限")
        else:
            if not set(code).issubset(set(user.permission_codes)):  # 判断一个列表中是否包含另一个列表中的元素
                raise UserErrors(code=status.HTTP_403_FORBIDDEN, err_desc="没有权限")

    return wrapper


# https://fastapi.tiangolo.com/tutorial/dependencies/
GetDB = Annotated[Session, Depends(get_db)]
CheckCookie = Annotated[LocalUser, Depends(check_cookie)]
