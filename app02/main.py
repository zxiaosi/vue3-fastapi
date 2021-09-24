#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:04
# @Author : 小四先生
# @desc : 主函数
from fastapi import FastAPI

from app02.core.config import settings
from app02.db.session import engine
from app02.db import base

# 配置接口文档信息
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

# 创建 db/base 下的所有表
base.Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)