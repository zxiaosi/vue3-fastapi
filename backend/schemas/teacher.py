#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : JSON字段验证[教师表]
from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel, Field


# id 为 str 为了能够使用正则表达式匹配
# ... 表示必填, 和max_length冲突, 使用max_length可以输入空值
# Optional[str]: union[str, None] --> 表示 数据可以为str类型或者为空

# 共享JSON字段
class TeacherIn(BaseModel):
    name: str = Field(min_length=1, max_length=10, example='姓名', title='教师姓名')
    sex: Literal['man', 'woman'] = Field(default='man', example='性别: man->男, woman->女', title='教师性别')
    birthday: date = Field(default=date(2012, 1, 1), example='生日: 1998-7-2', title='教师生日')
    education: Literal['Bachelor', 'Master', 'Doctor'] = Field(
        default='Bachelor',
        example='学历：Bachelor->学士, Master->硕士, Doctor->博士',
        title='教师学历')
    title: Literal['Assistant', 'Lecturer', 'Associate', 'Professor'] = Field(
        default='Assistant',
        example='职称：Assistant->助教, Lecturer->讲师, Associate->副教授, Professor->教授',
        title='教师职称')
    department_id: str = Field(regex=r'^10[0-9]{2}$', min_length=4, max_length=4, example='院系编号', title='院系编号')


# 添加数据的JSON字段
class TeacherCreate(TeacherIn):
    id: str = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404', title='职工号')
    password: str = Field(..., max_length=60, example='教师密码', title='教师密码')


# 更新数据的JSON字段
class TeacherUpdate(TeacherIn):
    password: Optional[str] = None


# 查询数据的JSON字段
class TeacherOut(TeacherIn):
    id: Optional[str] = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404', title='职工号')

    class Config:
        orm_mode = True  # 是否使用orm模型
