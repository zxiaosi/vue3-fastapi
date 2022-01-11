#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 23:01
# @Author : zxiaosi
# @desc : 挂载其他app
from fastapi import FastAPI

from core import settings

# Admin接口文档配置
admin = FastAPI(
    title=settings.PROJECT_ADMIN_NAME,
    description=settings.PROJECT_ADMIN_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.PROJECT_DIR,
)

# Teacher接口文档配置
teacher = FastAPI(
    title=settings.PROJECT_TEACHER_NAME,
    description=settings.PROJECT_TEACHER_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.PROJECT_DIR,
)

# Student接口文档配置
student = FastAPI(
    title=settings.PROJECT_STUDENT_NAME,
    description=settings.PROJECT_STUDENT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.PROJECT_DIR,
)


def register_app(app: FastAPI):
    """ 挂在app """
    app.mount("/admin", admin)
    app.mount("/teacher", teacher)
    app.mount("/student", student)
