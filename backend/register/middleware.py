#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/6 14:29
# @Author : zxiaosi
# @desc : 中间件 https://fastapi.tiangolo.com/tutorial/middleware/
from fastapi import FastAPI, Request

from core import settings
from utils import logger, resp_401


# 折腾了很长时间,还是用依赖项解决吧

def register_middleware(app: FastAPI):
    """ 请求响应拦截 """

    @app.middleware("http")
    async def intercept(request: Request, call_next):
        # 得到真实ip https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        logger.info(f"访问记录:IP:{request.client.host}-method:{request.method}-url:{request.url}")
        await request.app.state.redis.incr('request_num')  # redis 存储的请求数量 (自增 1)

        # TODO 请求的方法多半是OPTIONS(预请求),暂时跳过token验证（暂时没有找到合适的方法解决）
        # nginx 解决跨域请求 https://segmentfault.com/a/1190000019227927
        if request.url.path in settings.FILTER_URI or request.method == 'OPTIONS':
            return await call_next(request)  # 返回请求(跳过token)
        else:
            token = request.headers.get('authorization')
            obj = await request.app.state.redis.get(token)
            if obj:
                return await call_next(request)  # 返回请求
            else:
                return resp_401(msg='token失效')
