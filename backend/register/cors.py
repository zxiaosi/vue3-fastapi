#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 10:04
# @Author : zxiaosi
# @desc : 解决跨域请求
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings


def register_cors(app: FastAPI):
    """ 跨域请求 -- https://fastapi.tiangolo.com/zh/tutorial/cors/ """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
