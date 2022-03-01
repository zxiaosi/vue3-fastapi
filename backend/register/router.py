#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 23:06
# @Author : zxiaosi
# @desc : 注册路由
from fastapi import FastAPI

from core import settings
from api import api_router


def register_router(app: FastAPI):
    """ 注册路由 """
    app.include_router(api_router, prefix=settings.API_PREFIX)
