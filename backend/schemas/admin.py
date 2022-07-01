#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 管理员表的模型
from typing import Optional

from pydantic import BaseModel, Field

from schemas import GMT


class AdminIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(..., max_length=10, example='姓名')
    image: str = Field(..., example='头像')
    address: str = Field(..., example='地址')


class AdminUpdate(AdminIn):
    """ 更新数据的字段验证 """
    password: Optional[str] = Field(max_length=60, example='管理员密码')  # 前端返回可不带该字段


class AdminCreate(AdminUpdate):
    """ 添加数据时的字段验证 """
    id: int = Field(..., example='自增编号')


class AdminOut(AdminIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='自增编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(个人理解: 放行,不验证)
