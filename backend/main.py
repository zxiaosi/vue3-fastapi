#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:04
# @Author : 小四先生
# @desc : 主函数
import uvicorn
from fastapi import FastAPI

from backend.api.api_v1.api import api_router
from backend.core.config import settings, logger
from backend.db import init_db
from backend.initial_data import sqlalchemy_orm_initial, sqlalchemy_core_initial

# 配置接口文档信息
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    # 日志初始化
    logger.info("日志初始化成功！！！")

    # 创建所有表
    init_db()

    # 两种初始化表数据的方式 (只能插入一次)
    # sqlalchemy_orm_initial()  # 速度略慢,性能正常
    sqlalchemy_core_initial()  # 速度与性能并行

    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
