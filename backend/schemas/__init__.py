#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : 小四先生
# @desc : Pydantic模型|架构 (数据验证)
""" 抛出Pydantic模型对象 """
from .user import User, UserCreate, UserInDB, UserUpdate
from .department import Department, DepartmentCreate, DepartmentInDB, DepartmentUpdate
from .major import Major, MajorCreate, MajorInDB, MajorUpdate
