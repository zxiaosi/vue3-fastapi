#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:04
# @Author : zxiaosi
# @desc : 主函数
import uvicorn
from fastapi import FastAPI

from core import settings
from db import init_db, sqlalchemy_core_initial, init_redis_pool
from register import register_router, register_cors, register_middleware, register_exception, register_mount
from utils import logger

# app
app = FastAPI(description=settings.PROJECT_DESC, version=settings.PROJECT_VERSION)


def create_app():
    """ 注册中心 """
    register_mount(app)  # 挂载静态文件

    register_exception(app)  # 注册捕获全局异常

    register_cors(app)  # 注册跨域请求

    register_middleware(app)  # 注册请求响应拦截

    register_router(app)  # 注册路由

    logger.info("日志初始化成功！！！")  # 初始化日志


@app.on_event("startup")
async def startup_event():
    create_app()  # 加载注册中心
    init_db()  # 初始化表
    sqlalchemy_core_initial()  # 初始化表数据
    app.state.redis = await init_redis_pool()  # redis


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()  # 关闭 redis


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
