#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : 小四先生
# @desc : Pydantic数据验证
""" 抛出Pydantic数据验证 """
from .user import User, UserCreate, UserInDB, UserUpdate
from .department import Department, DepartmentCreate, DepartmentInDB, DepartmentUpdate
from .major import Major, MajorCreate, MajorInDB, MajorUpdate
from .teacher import Teacher, TeacherCreate, TeacherInDB, TeacherUpdate
