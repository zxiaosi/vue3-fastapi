#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 16:58
# @Author : 小四先生
# @desc : 主函数
from fastapi import FastAPI

from app01.core.config import settings
from app01.db.session import engine
from app01.db import base

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

base.Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
