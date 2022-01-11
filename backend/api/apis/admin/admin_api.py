#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/4 16:38
# @Author : zxiaosi
# @desc : 管理员api汇总
from fastapi import APIRouter

from api.apis.admin import selectCourse, course, department, major, teacher, student

admin_api = APIRouter()
admin_api.include_router(department.router, prefix="/department")
admin_api.include_router(major.router, prefix="/major")
admin_api.include_router(teacher.router, prefix="/teacher")
admin_api.include_router(student.router, prefix="/student")
admin_api.include_router(course.router, prefix="/course")
admin_api.include_router(selectCourse.router, prefix="/selectCourse")
