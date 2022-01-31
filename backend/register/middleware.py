#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/6 14:29
# @Author : 小四先生
# @desc : 请求响应拦截
from fastapi import FastAPI
from starlette.requests import Request

from utils.logger import logger


def register_middleware(app: FastAPI):
    """ 请求响应拦截 hook https://fastapi.tiangolo.com/tutorial/middleware/ """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # 得到真实ip https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        # logger.info(f"访问记录:{request.method}-url:{request.url}\nheaders:{request.headers}\nIP:{request.client.host}")

        try:
            await request.app.state.redis.incr('request_num')  # redis 存储的请求数量 (自增 1)
        except Exception as e:
            logger.error(f'redis连接失败！--错误信息: {e}')
        logger.info(f"访问记录:IP:{request.client.host}-method:{request.method}-url:{request.url}")
        return await call_next(request)
