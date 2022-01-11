#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/9 17:06
# @Author : zxiaosi
# @desc : 学生api汇总
from fastapi import APIRouter

from api.apis.admin import department

student_api = APIRouter()
student_api.include_router(department.router, prefix="/department")
