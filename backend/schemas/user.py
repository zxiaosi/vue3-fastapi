#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:41
# @Author : 小四先生
# @desc : user的Pydantic数据验证
from typing import Optional
from pydantic import BaseModel
from pydantic.schema import datetime


# 共享属性
class UserBase(BaseModel):
    id: Optional[int] = None
    full_name: Optional[str] = None
    # sex: Optional[str] = None
    # birthday: Optional[datetime] = datetime.now()
    # is_active: Optional[bool] = True
    # is_superuser: bool = False


# 属性在创建时通过API接收
class UserCreate(UserBase):
    password: str


# 属性通过API接收更新
class UserUpdate(UserBase):
    password: Optional[str] = None


# 创建数据库
class UserInDBBase(UserBase):
    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加属性
class User(UserInDBBase):
    pass


# 存储在DB中的附加属性
class UserInDB(UserInDBBase):
    hashed_password: str
