#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : zxiaosi
# @desc : 接口汇总
from fastapi import APIRouter

from api.apis.admin import users, department, major, teacher, student, course, selectCourse
from api.apis import login, redis_check

api_router = APIRouter()

# redis
api_router.include_router(redis_check.router, tags=["Redis"])

# login
api_router.include_router(login.router, tags=["Login"])

# test
api_router.include_router(users.router, prefix="/users", tags=["Test-Users"])
# api_router.include_router(users.router, prefix="/users", tags=["users--用户表"], include_in_schema=False)  # 隐藏
# api_router.include_router(users.router, prefix="/users", tags=["users--用户表"], deprecated=True)  # 弃用

# admin
api_router.include_router(department.router, prefix="/department", tags=["Department"])
api_router.include_router(major.router, prefix="/major", tags=["Major"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["Teacher"])
api_router.include_router(student.router, prefix="/student", tags=["Student"])
api_router.include_router(course.router, prefix="/course", tags=["Course"])
api_router.include_router(selectCourse.router, prefix="/selectCourse", tags=["SelectCourse"])

# teacher

# student

__all__ = ["api_router"]
