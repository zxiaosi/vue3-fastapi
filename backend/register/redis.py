#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/31 14:42
# @Author : 小四先生
# @desc : Redis数据
from aioredis import Redis, from_url
from fastapi import FastAPI

from core.config import settings

DEFAULT_KEY_PREFIX = 'is-bitcoin-lit'


async def init_redis_pool() -> Redis:
    redis = await from_url(url=settings.REDIS_URI, encoding=settings.GLOBAL_ENCODING, decode_responses=True)
    return redis


class MoleculesRepository:
    """存储和检查 Reids Hash"""

    def __init__(self, redis: Redis):
        self._redis = redis

    async def set_multiple(self, key: str, smiles: dict):
        """
        将多个哈希字段设置为多个值.
        Dict可以作为第一个位置参数传递:
        哈希值是分子的正则表示
        哈希值是分子类型，即SMILE
        :param key:
        :param smiles:
        :return:
        """
        return await self._redis.hmset(key, smiles)

    async def len(self, key: str):
        """
        获取给定hash中的字段数.
        :param key:
        :return: int:
        """
        return await self._redis.hlen(key)

    async def get_all(self, key: str):
        """
        获取hash中的所有字段和值
        :param key:
        :return: dict:
        """
        return await self._redis.hgetall(key)


def register_redis(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await init_redis_pool()
        app.state.mols_repo = MoleculesRepository(app.state.redis)

    @app.on_event("shutdown")
    async def shutdown_event():
        await app.state.redis.close()
