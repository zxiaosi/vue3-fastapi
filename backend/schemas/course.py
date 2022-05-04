#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 课程表模型
from pydantic import BaseModel, Field
from schemas import GMT


class CourseIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(min_length=1, max_length=20, example='课程名字')
    credit: float = Field(..., example='学分')
    period: int = Field(..., example='课时')


class CourseCreate(CourseIn):
    """ 添加数据时的字段验证 """
    id: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101')


class CourseUpdate(CourseIn):
    """ 更新数据的字段验证 """
    pass


class CourseOut(CourseCreate, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
