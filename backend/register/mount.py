#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 11:21
# @Author : zxiaosi
# @desc : 挂载静态文件
import os
from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from core.config import settings


def register_mount(app: FastAPI):
    """ 挂载静态文件 -- https://fastapi.tiangolo.com/zh/tutorial/static-files/ """

    path = Path(settings.STATIC_DIR).absolute().parent / settings.STATIC_DIR  # 拼接日志文件夹的路径
    os.makedirs(path, exist_ok=True)  # 如果文件夹不存在就创建

    # 第一个参数为url路径参数, 第二参数为静态文件目录的路径, 第三个参数是FastAPI内部使用的名字
    app.mount(f"/{settings.STATIC_DIR}", StaticFiles(directory=settings.STATIC_DIR), name=settings.STATIC_DIR)
