#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/22 16:40
# @Author : zxiaosi
# @desc : 日志表的模型
from pydantic import BaseModel, Field


class SysLogIn(BaseModel):
    """ 共享数据模型 """
    url: str = Field(example='请求url')
    method: str = Field(example='请求方法')
    ip: str = Field(example='请求ip')
    params: str | None = Field(example='请求参数')
    spend_time: str | None = Field(example='响应时间')
    create_time: str | None = Field(example='创建时间')


class SysLogOut(SysLogIn):
    """ 查询数据的数据模型 """
    id: int

    class Config:
        orm_mode = True  # 支持映射到ORM对象的模型
