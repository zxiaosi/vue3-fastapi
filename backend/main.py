#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:04
# @Author : 小四先生
# @desc : 主函数
import time

import uvicorn
from fastapi import FastAPI

from backend.core.config import settings, logger
from db.init_db import init_db
from initial_data.init_data import sqlalchemy_orm_initial, sqlalchemy_core_initial

# 配置接口文档信息
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

if __name__ == '__main__':
    # 日志初始化
    logger.info("日志初始化成功！！！")

    # 创建所有表
    init_db()

    # 两种初始化表数据的方式 (只能插入一次)
    # sqlalchemy_orm_initial()  # 速度略慢,性能正常
    time.sleep(2)
    sqlalchemy_core_initial()  # 速度与性能并行

    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
