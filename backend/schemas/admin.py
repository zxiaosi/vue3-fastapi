#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 管理员表的模型
from typing import Union
from pydantic import BaseModel, Field

from core import settings
from schemas import GMT


class AdminIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(..., max_length=10, example='姓名')
    image: str = Field(default=f'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg', example='头像')
    address: str = Field(default='广东省广州市', example='地址')


class AdminCreate(AdminIn):
    """ 添加数据时的字段验证 """
    password: str = Field(default='123456', max_length=60, example='管理员密码')  # 未输入密码,默认为'123456'


class AdminUpdate(AdminIn):
    """ 更新数据的字段验证 """
    password: Union[str]  # 未输入密码,默认为''(为原密码)


class AdminOut(AdminIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='自增编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(个人理解: 放行,不验证)
