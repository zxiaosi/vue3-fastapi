#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 选课表模型
from pydantic import BaseModel, Field

from schemas import GMT


class SelectCourseIn(BaseModel):
    """ 共享模型字段 """
    grade: str = Field(default=0, regex=r'^100|(^([0]{0})([1-9]{0,1})([0-9]{1}))$', max_length=3, example='成绩')
    student_id: str = Field(regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401')
    teacher_id: str = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404')
    course_id: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101')


class SelectCourseCreate(SelectCourseIn):
    """ 添加数据时的字段验证 """
    pass


class SelectCourseUpdate(SelectCourseIn):
    """ 更新数据的字段验证 """
    pass


class SelectCourseOut(SelectCourseIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='自增编号')
    student_id: int = Field(..., example='学号')
    teacher_id: int = Field(..., example='职工号')
    course_id: int = Field(..., example='课程号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
