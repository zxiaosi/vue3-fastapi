#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/4 16:38
# @Author : zxiaosi
# @desc : 教师api汇总
from fastapi import APIRouter

from api.apis.admin import department

teacher_api = APIRouter()
teacher_api.include_router(department.router, prefix="/department")
