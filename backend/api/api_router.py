#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : zxiaosi
# @desc : 接口汇总
from fastapi import APIRouter, Depends

from api.admin import department, major, teacher, student, course, selectCourse, dashBoard
from api.common import login, redis_check, upload
from api.deps import get_token

api_router = APIRouter()

# include_in_schema=False 隐藏属性
# deprecated=True 弃用属性

# Redis
api_router.include_router(redis_check.router, tags=["Redis"])

# Login
api_router.include_router(login.router, tags=["Login"])

# Upload
api_router.include_router(upload.router, tags=["Upload"], dependencies=[Depends(get_token)])

# Dashboard(需要token)
api_router.include_router(dashBoard.router, tags=["Dashboard"])

# Admin(需要token)
api_router.include_router(department.router, prefix="/department", tags=["Department"],
                          dependencies=[Depends(get_token)])
api_router.include_router(major.router, prefix="/major", tags=["Major"], dependencies=[Depends(get_token)])
api_router.include_router(teacher.router, prefix="/teacher", tags=["Teacher"], dependencies=[Depends(get_token)])
api_router.include_router(student.router, prefix="/student", tags=["Student"], dependencies=[Depends(get_token)])
api_router.include_router(course.router, prefix="/course", tags=["Course"], dependencies=[Depends(get_token)])
api_router.include_router(selectCourse.router, prefix="/selectCourse", tags=["SelectCourse"],
                          dependencies=[Depends(get_token)])

# teacher

# student
