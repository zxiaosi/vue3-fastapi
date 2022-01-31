#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:04
# @Author : zxiaosi
# @desc : 主函数
import uvicorn
from fastapi import FastAPI

from core import settings
from db import init_db
from initial_data import sqlalchemy_core_initial, sqlalchemy_orm_initial
from register import register_app, register_cors, register_exception, register_router, register_redis
from register.middleware import register_middleware
from utils import logger

# 接口文档配置
app = FastAPI(description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)

# 挂载其他app
register_app(app)

# 注册路由
register_router(app)

# 注册跨域请求
register_cors(app)

# 注册Redis
register_redis(app)

# 注册请求响应拦截
register_middleware(app)

# 注册捕获全局异常
register_exception(app)

if __name__ == '__main__':
    logger.info("日志初始化成功！！！")

    # 创建所有表
    init_db()

    # 两种初始化表数据的方式 (只能插入一次)
    # sqlalchemy_orm_initial()  # 速度略慢,性能正常
    sqlalchemy_core_initial()  # 速度与性能并行

    # Docker启动方式
    # uvicorn.run(app='main:app', host="0.0.0.0", port=8000)
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
