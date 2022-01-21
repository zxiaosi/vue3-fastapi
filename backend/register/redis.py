#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/31 14:42
# @Author : 小四先生
# @desc : Redis数据
from fastapi import FastAPI

from utils import init_redis_pool, MoleculesRepository


def register_redis(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await init_redis_pool()
        app.state.mol_repo = MoleculesRepository(app.state.redis)

    @app.on_event("shutdown")
    async def shutdown_event():
        await app.state.redis.close()
