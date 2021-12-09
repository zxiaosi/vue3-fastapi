#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : 小四先生
# @desc : 学生表的Pydantic数据验证
from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel, Field


# 共享JSON字段属性
class StudentBase(BaseModel):
    id: str = Field(regex=r'^[1-9]\d{9}$', min_length=10, max_length=10, example='学号：1810020401', title='学号')
    name: str = Field(max_length=10, example='姓名', title='学生姓名')
    sex: Literal['man', 'woman'] = Field(example='性别：man->男, woman->女', title='学生性别')
    birthday: date = Field(example='生日: 1998-7-2', title='学生生日')
    major_id: str = Field(regex=r'^10\d{4}$', min_length=6, max_length=6, example='专业编号', title='专业编号')


# 通过API创建时接收的JSON字段
class StudentCreate(StudentBase):
    """ 通过API创建时接收的JSON字段 """
    password: str = Field(max_length=60, example='学生密码', title='学生密码')


# 通过API更新时接收的JSON字段
class StudentUpdate(StudentBase):
    """ 通过API更新时接收的JSON字段 """
    password: Optional[str] = None


# 创建数据库
class StudentInDBBase(StudentBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加JSON字段
class StudentReturn(StudentInDBBase):
    """ 通过API返回的附加JSON字段 """
    pass


# 存储在DB中的附加JSON字段
class StudentInDB(StudentInDBBase):
    """ 存储在DB中的附加JSON字段 """
    hashed_password: str = Field(max_length=60, example='学生密码', title='学生密码')
