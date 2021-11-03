#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:59
# @Author : 小四先生
# @desc : 院系表模型的数据验证
# 共享属性
from typing import Optional

from pydantic import BaseModel


# 共享属性
class DepartmentBase(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    chairman: Optional[str] = None
    phone: Optional[str] = None


# 属性在创建时通过API接收
class DepartmentCreate(DepartmentBase):
    pass


# 属性通过API接收更新
class DepartmentUpdate(DepartmentBase):
    pass


# 创建数据库
class DepartmentInDBBase(DepartmentBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加属性
class Department(DepartmentInDBBase):
    pass


# 存储在DB中的附加属性
class DepartmentInDB(DepartmentInDBBase):
    pass
