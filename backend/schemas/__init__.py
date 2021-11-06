#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : 小四先生
# @desc : 返回和接收的JSON字段以及数据验证
""" 抛出JSON字段模型对象 """
from .user import User, UserCreate, UserInDB, UserUpdate
from .department import Department, DepartmentCreate, DepartmentInDB, DepartmentUpdate
from .major import Major, MajorCreate, MajorInDB, MajorUpdate
