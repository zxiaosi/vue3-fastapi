#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 11:04
# @Author : zxiaosi
# @desc : 注册路由
from fastapi import FastAPI, Depends

from apis import hello, user
from common import check_permission
from core.config import settings


def register_router(app: FastAPI):
    """ 注册路由 """

    app.include_router(hello.router, prefix=settings.API_PREFIX, tags=["Hello"])

    app.include_router(user.router, prefix=settings.API_PREFIX + "/user", tags=["User"],
                       dependencies=[Depends(check_permission([]))])
