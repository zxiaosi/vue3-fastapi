#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/18 19:38
# @Author : zxiaosi
# @desc : redis
import json
from typing import Union
from aioredis import Redis, from_url

from core.config import settings


# 参考: https://github.com/grillazz/fastapi-redis/tree/main/app
async def init_redis_pool() -> Redis:
    """ 连接redis """
    redis = await from_url(url=settings.REDIS_URI, encoding=settings.GLOBAL_ENCODING, decode_responses=True)
    return redis


class MoleculesRepository:
    """存储和检查 Reids 的方法"""

    def __init__(self, redis: Redis):
        self._redis = redis

    async def dumps(self, data: Union[str, list, dict]) -> str:
        """ 将对象转为字符串 """
        return json.dumps(data)

    async def loads(self, data: str) -> object:
        """ 将字符串转为对象 """
        return json.loads(data)

    async def list_loads(self, key: str) -> list:
        """ 将列表字符串转为对象 """
        todo_list = await self._redis.lrange(key, 0, -1)
        return [json.loads(todo) for todo in todo_list]
