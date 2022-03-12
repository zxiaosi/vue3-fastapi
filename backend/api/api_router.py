#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : zxiaosi
# @desc : 接口汇总
from fastapi import APIRouter

from api.admin import department, major, teacher, student, course, selectCourse, dashBoard
from api.common import upload

admin_router = APIRouter()

# include_in_schema=False 隐藏属性
# deprecated=True 弃用属性

# 上传图片
admin_router.include_router(upload.router, tags=["Upload"])

# 首页
admin_router.include_router(dashBoard.router, tags=["Dashboard"])

# Admin
admin_router.include_router(department.router, prefix="/department", tags=["Department"])
admin_router.include_router(major.router, prefix="/major", tags=["Major"])
admin_router.include_router(teacher.router, prefix="/teacher", tags=["Teacher"])
admin_router.include_router(student.router, prefix="/student", tags=["Student"])
admin_router.include_router(course.router, prefix="/course", tags=["Course"])
admin_router.include_router(selectCourse.router, prefix="/selectCourse", tags=["SelectCourse"])

# teacher

# student
