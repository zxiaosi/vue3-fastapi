#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/6 14:29
# @Author : zxiaosi
# @desc : 中间件 https://fastapi.tiangolo.com/tutorial/middleware/
from fastapi import FastAPI, Request

from utils import logger


# 得到真实ip https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
# nginx 解决跨域请求 https://segmentfault.com/a/1190000019227927

def register_middleware(app: FastAPI):
    """ 请求拦截与响应拦截 """

    @app.middleware("http")
    async def intercept(request: Request, call_next):
        logger.info(f"访问记录:IP:{request.client.host}-method:{request.method}-url:{request.url}")
        await request.app.state.redis.incr('request_num')  # redis 请求数量 (自增 1)
        return await call_next(request)  # 返回请求(跳过token)
