#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 17:18
# @Author : 小四先生
# @desc : user蓝图
from typing import Optional
from pydantic import BaseModel, EmailStr


# 共享属性
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# 属性在创建时通过API接收
class UserCreate(UserBase):
    email: EmailStr
    password: str


# 属性通过API接收更新
class UserUpdate(UserBase):
    password: Optional[str] = None


# 创建数据库
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加属性
class User(UserInDBBase):
    pass


# 存储在DB中的附加属性
class UserInDB(UserInDBBase):
    hashed_password: str
