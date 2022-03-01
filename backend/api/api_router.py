#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : zxiaosi
# @desc : 接口汇总
from fastapi import APIRouter

from api.admin import department, major, teacher, student, course, selectCourse, index
from api.common import login, redis_check

api_router = APIRouter()

# include_in_schema=False 隐藏属性
# deprecated=True 弃用属性

# redis
api_router.include_router(redis_check.router, tags=["Redis"])
api_router.include_router(index.router, tags=["Dashboard"])

# login
api_router.include_router(login.router, tags=["Login"])

# admin
api_router.include_router(department.router, prefix="/department", tags=["Department"])
api_router.include_router(major.router, prefix="/major", tags=["Major"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["Teacher"])
api_router.include_router(student.router, prefix="/student", tags=["Student"])
api_router.include_router(course.router, prefix="/course", tags=["Course"])
api_router.include_router(selectCourse.router, prefix="/selectCourse", tags=["SelectCourse"])

# teacher

# student
