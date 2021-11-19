#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : 小四先生
# @desc : 课程表的Pydantic数据验证
from pydantic import BaseModel, Field


# 共享JSON字段属性
class CourseBase(BaseModel):
    id: str = Field(regex=r'^[1-9]\d{3}$', min_length=4, max_length=4, example='课程编号：1101', title='课程编号')
    name: str = Field(max_length=20, example='课程名字', title='课程名字')
    credit: float = Field(example='学分', title='学分')
    period: int = Field(example='课时', title='课时')


# 通过API创建时接收的JSON字段
class CourseCreate(CourseBase):
    """ 通过API创建时接收的JSON字段 """
    pass


# 通过API更新时接收的JSON字段
class CourseUpdate(CourseBase):
    """ 通过API更新时接收的JSON字段 """
    pass


# 创建数据库
class CourseInDBBase(CourseBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加JSON字段
class CourseReturn(CourseInDBBase):
    """ 通过API返回的附加JSON字段 """
    pass


# 存储在DB中的附加JSON字段
class CourseInDB(CourseInDBBase):
    """ 存储在DB中的附加JSON字段 """
    pass
