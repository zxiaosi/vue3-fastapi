#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 讲授表模型
from pydantic import BaseModel, Field

from schemas import GMT


class TaughtIn(BaseModel):
    """ 共享模型字段 """
    teacherId: str = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404')
    courseId: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101')


class TaughtCreate(TaughtIn):
    """ 添加数据时的字段验证 """
    pass


class TaughtUpdate(TaughtIn):
    """ 更新数据的字段验证 """
    pass


class TaughtOut(TaughtIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='自增编号')
    teacherId: int = Field(..., example='职工号')
    courseId: int = Field(..., example='课程号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
