#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/6/26 22:39
# @Author : zxiaosi
# @desc : 依赖项
from starlette.requests import Request


async def get_redis(request: Request):
    return request.app.state.redis
