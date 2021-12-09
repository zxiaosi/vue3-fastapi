#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : 小四先生
# @desc : 教师表的Pydantic数据验证
from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel, Field


# 共享JSON字段属性
class TeacherBase(BaseModel):
    id: str = Field(regex=r'^[1-9]\d{5}$', min_length=6, max_length=6, example='职工号：180404', title='职工号')
    name: str = Field(max_length=10, example='姓名', title='教师姓名')
    sex: Literal['man', 'woman'] = Field(example='性别：man->男, woman->女', title='教师性别')
    birthday: date = Field(example='生日: 1998-7-2', title='教师生日')
    education: Literal['Bachelor', 'Master', 'Doctor'] = Field(example='学历：Bachelor->学士, Master->硕士, Doctor->博士',
                                                               title='教师学历')
    title: Literal['Assistant', 'Lecturer', 'Associate', 'Professor'] = Field(
        example='职称：Assistant->助教, Lecturer->讲师, Associate->副教授, Professor->教授',
        title='教师职称')
    department_id: str = Field(regex=r'^10\d{2}$', min_length=4, max_length=4, example='院系编号', title='院系编号')


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
class TeacherReturn(TeacherInDBBase):
    """ 通过API返回的附加JSON字段 """
    pass


# 存储在DB中的附加JSON字段
class TeacherInDB(TeacherInDBBase):
    """ 存储在DB中的附加JSON字段 """
    hashed_password: str = Field(max_length=60, example='教师密码', title='教师密码')
