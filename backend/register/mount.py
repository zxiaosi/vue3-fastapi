#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 11:21
# @Author : zxiaosi
# @desc : 挂载静态文件
import os
from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from core.config import settings, FileDirEnum


def register_mount(app: FastAPI):
    """ 挂载静态文件 -- https://fastapi.tiangolo.com/zh/tutorial/static-files/ """

    current_path = Path(settings.STATIC_DIR).absolute().parent  # 获取当前文件夹的上一级目录
    for path in [current_path / FileDirEnum.AVATAR.value, current_path / FileDirEnum.ICON.value]:
        os.makedirs(path, exist_ok=True)  # 如果文件夹不存在就创建

    # 第一个参数为url路径参数, 第二参数为静态文件目录的路径, 第三个参数是FastAPI内部使用的名字
    app.mount(f"/{settings.STATIC_DIR}", StaticFiles(directory=settings.STATIC_DIR), name=settings.STATIC_DIR)
    app.mount(f"/{FileDirEnum.AVATAR.value}", StaticFiles(directory=FileDirEnum.AVATAR.value),
              name=FileDirEnum.AVATAR.value)
    app.mount(f"/{FileDirEnum.ICON.value}", StaticFiles(directory=FileDirEnum.ICON.value), name=FileDirEnum.ICON.value)
