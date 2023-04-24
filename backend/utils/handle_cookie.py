#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/21 23:26
# @Author : zxiaosi
# @desc : 设置、清除 Cookie
from pydantic import BaseModel
from starlette.responses import Response

from core.config import settings
from core.security import get_cookie_hash
from models import LocalUser


def set_cookie(key: str, user: dict | BaseModel, response: Response):
    """ 设置 Cookie """
    session = get_cookie_hash(key)  # 生成session

    _user = user if isinstance(user, dict) else user.dict()  # ORM对象转字典

    LocalUser(**_user, pk=session).save().expire(settings.REDIS_EXPIRE)  # 生成redis-orm对象, 保存到redis中, 设置过期时间

    response.set_cookie(key=settings.COOKIE_KEY, value=session, expires=settings.COOKIE_MAX_AGE, httponly=False)


def clear_cookie(response: Response):
    """ 清除 Cookie """
    response.delete_cookie(settings.COOKIE_KEY)
