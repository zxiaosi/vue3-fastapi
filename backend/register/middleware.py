#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 10:25
# @Author : zxiaosi
# @desc : 中间件
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response


def register_middleware(app: FastAPI):
    """ 请求拦截与响应拦截 -- https://fastapi.tiangolo.com/tutorial/middleware/ """

    @app.middleware("http")
    async def intercept(request: Request, call_next) -> Response:
        """
            在这里获取 request.body() 出现了问题...
            使用了自定义路由APIRoute https://fastapi.tiangolo.com/advanced/custom-request-and-route/#custom-apiroute-class-in-a-router
        """
        return await call_next(request)
