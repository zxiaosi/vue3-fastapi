#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:59
# @Author : 小四先生
# @desc : 院系表的Pydantic数据验证
# 共享属性
from typing import Optional

from pydantic import BaseModel, Field


# 共享JSON字段属性
class DepartmentBase(BaseModel):
    id: str = Field(regex=r'^10', min_length=4, max_length=4, example='院系编号', title='院系编号')
    name: str = Field(max_length=20, example='院系名字', title='院系名字')
    chairman: str = Field(max_length=10, example='主任名', title='主任名')
    phone: Optional[str] = Field(default=None, max_length=11, example='主任手机号', title='主任手机号')  # 默认值为空


# 通过API创建时接收的JSON字段
class DepartmentCreate(DepartmentBase):
    """ 通过API创建时接收的JSON字段 """
    pass


# 通过API更新时接收的JSON字段
class DepartmentUpdate(DepartmentBase):
    """ 通过API更新时接收的JSON字段 """
    pass


# 创建数据库
class DepartmentInDBBase(DepartmentBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加JSON字段
class Department(DepartmentInDBBase):
    """ 通过API返回的附加JSON字段 """
    pass


# 存储在DB中的附加JSON字段
class DepartmentInDB(DepartmentInDBBase):
    """ 存储在DB中的附加JSON字段 """
    pass
