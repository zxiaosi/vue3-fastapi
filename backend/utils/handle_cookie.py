#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/21 23:26
# @Author : zxiaosi
# @desc : 设置、清除 Cookie
from starlette.responses import Response

from core.config import settings
from core.security import get_cookie_hash
from models import LocalUser


def set_cookie(key: str, user: LocalUser, response: Response):
    """ 设置 Cookie """
    session = get_cookie_hash(key)  # 生成session

    _user = user.dict(exclude={"pk"})  # 将用户信息转换为字典, 并排除 pk

    LocalUser(**_user, pk=session).save().expire(settings.REDIS_EXPIRE)  # 生成redis-orm对象, 保存到redis中, 设置过期时间

    response.set_cookie(key=settings.COOKIE_KEY, value=session, expires=settings.COOKIE_MAX_AGE, httponly=False)


def clear_cookie(response: Response):
    """ 清除 Cookie """
    response.delete_cookie(settings.COOKIE_KEY)
