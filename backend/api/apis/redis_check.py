#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/5 13:55
# @Author : zxiaosi
# @desc : 测试redis
from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


@router.get("/health-check")
async def health_check(request: Request):
    try:
        # key:test:keys => key/test/keys
        await request.app.state.redis.set('key:test:keys', 'value')
        value = await request.app.state.redis.get('key')
    except Exception as e:  # noqa: E722
        print("对不起,不能打开Redis!!!", e)
        value = 'down'
    return {"web_server": "up", "request": value}
