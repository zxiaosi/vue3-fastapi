#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : 小四先生
# @desc : 选课表的Pydantic数据验证
from pydantic import BaseModel, Field


# 共享JSON字段属性
class SelectCourseBase(BaseModel):
    grade: str = Field(default=0, regex=r'^100|(^([1-9]{0,1})([0-9]{1}))$', max_length=3, example='成绩', title='成绩')
    student_id: str = Field(regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401', title='学号')
    teacher_id: str = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404', title='职工号')
    course_id: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101', title='课程编号')


# 通过API创建时接收的JSON字段
class SelectCourseCreate(SelectCourseBase):
    """ 通过API创建时接收的JSON字段 """
    pass


# 通过API更新时接收的JSON字段
class SelectCourseUpdate(SelectCourseBase):
    """ 通过API更新时接收的JSON字段 """
    pass


# 创建数据库
class SelectCourseInDBBase(SelectCourseBase):
    id: int = Field(default='999', example='自增编号', title='编号')

    class Config:
        orm_mode = True  # 是否为orm模型


# 通过API返回的附加JSON字段
class SelectCourseReturn(SelectCourseInDBBase):
    """ 通过API返回的附加JSON字段 """
    pass


# 存储在DB中的附加JSON字段
class SelectCourseInDB(SelectCourseInDBBase):
    """ 存储在DB中的附加JSON字段 """
    pass
