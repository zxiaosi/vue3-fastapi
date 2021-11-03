#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : 小四先生
# @desc : 接口汇总
from fastapi import APIRouter

from api.api_v1.endpoints import users, department, major

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users--用户表"])
api_router.include_router(department.router, prefix="/department", tags=["department--院系表"])
api_router.include_router(major.router, prefix="/major", tags=["major--专业表"])
