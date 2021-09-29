#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:04
# @Author : 小四先生
# @desc : 主函数
import uvicorn
from fastapi import FastAPI

from app02.core.config import settings
from app02.db.init_db import init_db, drop_db
from app02.initial_data.init_data import sqlalchemy_orm_initial, sqlalchemy_core_initial

# 配置接口文档信息
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

if __name__ == '__main__':
    # 表的初始化
    init_db()

    # 两种初始化表数据的方式 (只能插入一次)
    # sqlalchemy_orm_initial()  # 速度略慢,性能正常
    sqlalchemy_core_initial()  # 速度与性能并行

    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)