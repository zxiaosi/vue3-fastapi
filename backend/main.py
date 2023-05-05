#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/28 17:27
# @Author : zxiaosi
import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.init_db import init_table, init_data
from register import register_mount, register_exception, register_router, register_cors
from common.custom_log import my_logger

app = FastAPI(description=settings.PROJECT_DESC, version=settings.PROJECT_VERSION)

register_cors(app)  # 注册跨域请求

register_mount(app)  # 挂载静态文件

register_router(app)  # 注册路由

register_exception(app)  # 注册异常捕获

# register_middleware(app)  # 注册请求响应拦截

init_table()  # 初始化表
init_data()  # 初始化表数据

my_logger.info("项目启动成功！！！")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
