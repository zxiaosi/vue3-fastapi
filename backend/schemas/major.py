#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : 小四先生
# @desc : 专业表的Pydantic数据验证
# 共享属性
from typing import Optional

from pydantic import BaseModel, Field


# 共享JSON字段属性
class MajorBase(BaseModel):
    id: str = Field(regex=r'^10', min_length=6, max_length=6, example='专业编号', title='专业编号')
    name: str = Field(max_length=20, example='专业名字', title='专业名字')
    assistant: str = Field(max_length=10, example='辅导员名', title='辅导员名')
    phone: Optional[str] = Field(default=None, max_length=11, example='辅导员手机号', title='辅导员手机号')  # 默认值为空
    department_id: str = Field(regex=r'^10', min_length=4, max_length=4, example='院系编号', title='院系编号')


# 通过API创建时接收的JSON字段
class MajorCreate(MajorBase):
    """ 通过API创建时接收的JSON字段 """
    pass


# 通过API更新时接收的JSON字段
class MajorUpdate(MajorBase):
    """ 通过API更新时接收的JSON字段 """
    pass


# 创建数据库
class MajorInDBBase(MajorBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加JSON字段
class Major(MajorInDBBase):
    """ 通过API返回的附加JSON字段 """
    department_name: Optional[str] = Field(default=None, max_length=20, example='院系名字', title='院系名字')


# 存储在DB中的附加JSON字段
class MajorInDB(MajorInDBBase):
    """ 存储在DB中的附加JSON字段 """
    pass
