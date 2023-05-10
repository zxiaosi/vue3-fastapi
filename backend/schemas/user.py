#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 18:43
# @Author : zxiaosi
# @desc : 用户表模型
from pydantic import BaseModel, Field

from schemas.gmt import GMT


class UserIn(BaseModel):
    """ 共享数据模型 """
    name: str = Field(example='用户名')
    avatar: str | None = Field(example='头像')
    sex: int | None = Field(default=0, ge=0, le=2, example='性别: 0 未知 1 男 2 女')
    phone: str | None = Field(example='手机号')


class UserCreate(UserIn):
    """ 添加数据时的数据模型 """
    password: str | None = Field(max_length=60, example='密码')  # 前端返回可不带该字段


class UserUpdate(UserCreate):
    """ 更新数据的数据模型 """
    pass


class UserOut(UserIn, GMT):
    """ 查询数据的数据模型 """
    id: int
    version: int
    is_deleted: int
    role_name: str | None = Field(example='角色名')

    class Config:
        orm_mode = True  # 支持映射到ORM对象的模型


class UserLogin(BaseModel):
    """ 登录 """
    name: str = Field(example='用户名')
    password: str = Field(example='密码')


class LocalUserSchema(UserIn):
    """ 本地用户模型(用于比较) """
    version: int
    is_deleted: int

    class Config:
        orm_mode = True
