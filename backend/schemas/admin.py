#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 管理员表的模型
from typing import Literal, Optional
from pydantic import BaseModel, Field

from schemas import GMT


class AdminIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(..., max_length=10, example='姓名')
    sex: Literal['man', 'woman'] = Field(..., example='性别：man->男, woman->女')


class AdminCreate(AdminIn):
    """ 添加数据时的字段验证 """
    password: str = Field(default='123456', max_length=60, example='管理员密码')


class AdminUpdate(AdminIn):
    """ 更新数据的字段验证 """
    password: Optional[str]


class AdminOut(AdminIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='自增编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(个人理解: 放行,不验证)
