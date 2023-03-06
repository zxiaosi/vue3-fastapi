#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 16:23
# @Author : zxiaosi
# @desc : 依赖项
from redis_om import NotFoundError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from starlette.responses import Response

from core.config import settings
from models import LocalUser
from utils.custom_exc import BadCredentials
from utils.handle_cookie import clear_cookie

# 文档中介绍了四种 创建会话 的方式: https://docs.sqlalchemy.org/en/20/orm/session_basics.html

# 创建表引擎
engine = create_engine(
    url=settings.DATABASE_URI,  # 数据库uri
    echo=settings.DATABASE_ECHO,  # 是否打印日志
)

# 会话创建器
Session = sessionmaker(engine, expire_on_commit=False)


def get_db():
    """ 得到数据库的会话 """
    with Session() as session:  # 会话工厂(工厂对象帮助我们管理)
        yield session


def check_cookie(request: Request, response: Response):
    """ 校验cookie """
    if request.get("path") in settings.COOKIE_NOT_CHECK:  # 不校验Cookie
        return

    session = request.cookies.get(settings.COOKIE_KEY)
    try:
        return LocalUser.get(session)
    except NotFoundError:
        clear_cookie(response)
        raise BadCredentials()
