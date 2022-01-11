#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 管理员表的Pydantic数据验证
from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel, Field


# 共享JSON字段属性
class Admin(BaseModel):
    name: str = Field(..., max_length=10, example='姓名', title='管理员姓名')
    sex: Literal['man', 'woman'] = Field(..., example='性别：man->男, woman->女', title='管理员性别')
    password: str = Field(max_length=60, example='管理员密码', title='管理员密码')


# 存储到数据库JSON字段
class AdminInDB(Admin):
    id: int = Field(..., example='自增编号', title='编号')

    class Config:
        orm_mode = True  # 是否为orm模型
