#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : zxiaosi
# @desc : JSON字段验证[学生表]
from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel, Field


# id 为 str 为了能够使用正则表达式匹配
# ... 表示必填, 和max_length冲突, 使用max_length可以输入空值
# Optional[str]: union[str, None] --> 表示 数据可以为str类型或者为空

# 共享JSON字段
class StudentIn(BaseModel):
    name: str = Field(min_length=1, max_length=10, example='姓名', title='学生姓名')
    sex: Literal['man', 'woman'] = Field(default='man', example='性别：man->男, woman->女', title='学生性别')
    birthday: date = Field(default=date(2012, 1, 1), example='生日: 1998-7-2', title='学生生日')
    major_id: str = Field(regex=r'^10\d{4}$', min_length=6, max_length=6, example='专业编号', title='专业编号')


# 添加数据的JSON字段
class StudentCreate(StudentIn):
    id: str = Field(..., regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401', title='学号')
    password: str = Field(..., max_length=60, example='学生密码', title='学生密码')


# 更新数据的JSON字段
class StudentUpdate(StudentIn):
    password: Optional[str] = None


# 查询数据的JSON字段
class StudentOut(StudentIn):
    id: str = Field(..., regex=r'^[1-9][0-9]{9}$', min_length=10, max_length=10, example='学号：1810020401', title='学号')

    class Config:
        orm_mode = True  # 是否使用orm模型
