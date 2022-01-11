#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/9 16:48
# @Author : zxiaosi
# @desc : 跨域请求
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core import settings


def register_cors(app: FastAPI):
    """ 跨域请求 """
    if settings.CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
