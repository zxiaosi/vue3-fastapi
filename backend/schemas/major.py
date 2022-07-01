#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : zxiaosi
# @desc : 专业表模型
from typing import Optional
from pydantic import BaseModel, Field

from schemas import GMT


class MajorIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(max_length=20, example='名字')
    assistant: str = Field(min_length=1, max_length=10, example='辅导员名')
    phone: Optional[str] = Field(regex=r'(^\s{0}$)|^(0\d{2,3}-\d{7,8})|(1[34578]\d{9})$', example='辅导员手机号')
    departmentId: str = Field(regex=r'^10[0-9]{2}$', min_length=4, max_length=4, example='院系编号')


class MajorCreate(MajorIn):
    """ 添加数据时的字段验证 """
    id: str = Field(regex=r'^10[0-9]{4}$', min_length=6, max_length=6, example='编号')


class MajorUpdate(MajorIn):
    """ 更新数据的字段验证 """
    pass


class MajorOut(MajorIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='编号')
    departmentId: int = Field(..., example='院系编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
