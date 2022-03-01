#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/5 13:55
# @Author : zxiaosi
# @desc : 测试redis
from fastapi import APIRouter, Depends

from db import RedisPlus
from api.deps import get_redis, reusable_oauth2

router = APIRouter()


@router.get("/health-check")
async def health_check(token: str = Depends(reusable_oauth2), redis: RedisPlus = Depends(get_redis)):
    try:
        # key:test:keys => key/test/keys
        value = await redis.get('request_num')
        msg = "开启Redis成功！！！"
    except Exception as e:  # noqa: E722
        value = 0
        msg = f"对不起,不能打开Redis!!! {e}"
    return {"request": f"总计请求次数 {value}", "msg": msg}
