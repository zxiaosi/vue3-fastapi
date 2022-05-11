#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : zxiaosi
# @desc : 接口汇总
from fastapi import APIRouter

from apis.common import upload, student, teacher, department, major, course, taught, elective

app_router = APIRouter()

# include_in_schema=False 隐藏属性
# deprecated=True 弃用属性

# 上传图片
app_router.include_router(upload.router, tags=["Upload"])

# common
app_router.include_router(elective.router, prefix="/elective", tags=["elective"])
app_router.include_router(department.router, prefix="/department", tags=["Department"])
app_router.include_router(major.router, prefix="/major", tags=["major"])
app_router.include_router(course.router, prefix="/course", tags=["course"])
app_router.include_router(teacher.router, prefix="/teacher", tags=["teacher"])
app_router.include_router(student.router, prefix="/student", tags=["student"])
app_router.include_router(taught.router, prefix="/taught", tags=["taught"])


# Admin

# teacher

# student
