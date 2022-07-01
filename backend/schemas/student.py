#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : zxiaosi
# @desc : 学生表模型
from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel, Field

from schemas import GMT


class StudentIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(min_length=1, max_length=10, example='姓名')
    sex: Literal['0', '1'] = Field(..., example='性别：0->男, 1->女')
    birthday: date = Field(..., example='生日: 1998-7-2')
    image: str = Field(..., example='头像')
    address: str = Field(..., example='地址')
    majorId: str = Field(regex=r'^10\d{4}$', min_length=6, max_length=6, example='专业编号')


class StudentUpdate(StudentIn):
    """ 更新数据的字段验证 """
    password: Optional[str] = Field(max_length=60, example='密码')  # 前端返回可不带该字段


class StudentCreate(StudentUpdate):
    """ 添加数据时的字段验证 """
    id: str = Field(regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401')


class StudentOut(StudentIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='学号：1810020401')
    majorId: int = Field(..., example='专业编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
