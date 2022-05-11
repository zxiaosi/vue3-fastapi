#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 23:06
# @Author : zxiaosi
# @desc : 注册路由
from fastapi import FastAPI, Security

from core import settings
from apis import app_router
from apis.deps import get_current_user
from apis.common import redis_check, login, dashboard


def register_router(app: FastAPI):
    """ 注册路由 """

    app.include_router(redis_check.router, prefix=settings.API_PREFIX, tags=["Redis"])  # Redis(不需要权限)

    app.include_router(login.router, prefix=settings.API_PREFIX, tags=["Login"])  # Login(权限在每个接口上)

    app.include_router(dashboard.router, prefix=settings.API_PREFIX, tags=["Dashboard"],
                       dependencies=[Security(get_current_user, scopes=[])])  # Dashboard(不需要权限,但需要登录)

    # 权限(权限在每个接口上)
    app.include_router(app_router, prefix=settings.API_PREFIX)
