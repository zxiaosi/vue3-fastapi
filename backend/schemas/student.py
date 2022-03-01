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
    sex: Literal['man', 'woman'] = Field(default='man', example='性别：man->男, woman->女')
    birthday: date = Field(default=date(2012, 1, 1), example='生日: 1998-7-2')
    major_id: str = Field(regex=r'^10\d{4}$', min_length=6, max_length=6, example='专业编号')


class StudentCreate(StudentIn):
    """ 添加数据时的字段验证 """
    id: str = Field(..., regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401')
    password: str = Field(default='123456', max_length=60, example='学生密码')


class StudentUpdate(StudentIn):
    """ 更新数据的字段验证 """
    password: Optional[str]  # 如果为空,默认为上次保存的密码


class StudentOut(StudentIn, GMT):
    """ 查询数据的字段验证 """
    id: str = Field(..., regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401')

    class Config:
        orm_mode = True  # 是否使用orm模型(个人理解: 放行,不验证)
