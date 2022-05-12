#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 选课表模型
from typing import Optional

from pydantic import BaseModel, Field

from schemas import GMT


class ElectiveIn(BaseModel):
    """ 共享模型字段 """
    grade: Optional[str] = Field(regex=r'(^\s{0}$)|(^100)|(^([0]{0})([1-9]?)([0-9]))$', max_length=3, example='成绩')
    studentId: str = Field(regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401')
    courseId: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101')


class ElectiveCreate(ElectiveIn):
    """ 添加数据时的字段验证 """
    pass


class ElectiveUpdate(ElectiveIn):
    """ 更新数据的字段验证 """
    pass


class ElectiveOut(ElectiveIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='自增编号')
    studentId: int = Field(..., example='学号')
    courseId: int = Field(..., example='课程号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
