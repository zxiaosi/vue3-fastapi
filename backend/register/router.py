#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 23:06
# @Author : zxiaosi
# @desc : 注册路由
from fastapi import FastAPI, Security

from api.deps import get_current_user
from core import settings
from api import admin_router
from api.common import redis_check, login


def register_router(app: FastAPI):
    """ 注册路由 """
    # Redis
    app.include_router(redis_check.router, prefix=settings.API_PREFIX, tags=["Redis"])
    # Login
    app.include_router(login.router, prefix=settings.API_PREFIX, tags=["Login"])
    # Admin
    app.include_router(admin_router, prefix=settings.API_PREFIX,
                       dependencies=[Security(get_current_user, scopes=["admin"])])
