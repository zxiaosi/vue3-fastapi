#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : 小四先生
# @desc : 教师表的Pydantic数据验证
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


# 共享JSON字段属性
class TeacherBase(BaseModel):
    id: str = Field(min_length=6, max_length=6, example='职工号', title='职工号')
    name: str = Field(max_length=10, example='教师姓名', title='教师姓名')
    sex: str = Field(max_length=5, example='性别', title='教师性别')
    birthday: date = Field(example='教师生日: 1998-7-2', title='教师生日')
    education: str = Field(max_length=8, example='教师学历', title='教师学历')
    title: str = Field(max_length=9, example='教师职称', title='教师职称')
    department_id: str = Field(regex=r'^10', min_length=4, max_length=4, example='院系编号', title='院系编号')


# 通过API创建时接收的JSON字段
class TeacherCreate(TeacherBase):
    """ 通过API创建时接收的JSON字段 """
    password: str = Field(max_length=60, example='教师密码', title='教师密码')


# 通过API更新时接收的JSON字段
class TeacherUpdate(TeacherBase):
    """ 通过API更新时接收的JSON字段 """
    password: Optional[str] = None


# 创建数据库
class TeacherInDBBase(TeacherBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加JSON字段
class Teacher(TeacherInDBBase):
    """ 通过API返回的附加JSON字段 """
    department_name: Optional[str] = Field(default=None, max_length=20, example='院系名字', title='院系名字')


# 存储在DB中的附加JSON字段
class TeacherInDB(TeacherInDBBase):
    """ 存储在DB中的附加JSON字段 """
    hashed_password: str = Field(max_length=60, example='教师密码', title='教师密码')
