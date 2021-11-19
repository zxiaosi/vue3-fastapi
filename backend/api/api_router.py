#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : 小四先生
# @desc : 接口汇总
from fastapi import APIRouter

from api.apis import users, department, major, teacher, student, course, selectCourse

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users--用户表"], include_in_schema=False)  # 隐藏
# api_router.include_router(users.router, prefix="/users", tags=["users--用户表"], deprecated=True)  # 弃用
api_router.include_router(department.router, prefix="/department", tags=["department--院系表"])
api_router.include_router(major.router, prefix="/major", tags=["major--专业表"])
api_router.include_router(teacher.router, prefix="/teacher", tags=["teacher--教师表"])
api_router.include_router(student.router, prefix="/student", tags=["student--学生表"])
api_router.include_router(course.router, prefix="/course", tags=["course--课程表"])
api_router.include_router(selectCourse.router, prefix="/selectCourse", tags=["selectCourse--选课表"])
