#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 23:06
# @Author : zxiaosi
# @desc : 注册路由
from fastapi import FastAPI

from core import settings
from api import api_router
from api.apis import admin_api, teacher_api, student_api
from register.app import admin, teacher, student


def register_router(app: FastAPI):
    """ 注册路由 """
    app.include_router(api_router, prefix=settings.API_STR)
    admin.include_router(admin_api)
    teacher.include_router(teacher_api)
    student.include_router(student_api)
