#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : JSON字段验证[课程表]
from pydantic import BaseModel, Field


# id 使用 str 为了能够使用正则表达式匹配
# ... 表示必填, 和max_length冲突, 使用max_length可以输入空值
# Optional[str]: union[str, None] --> 表示 数据可以为str类型或者为空

# 共享JSON字段
class CourseIn(BaseModel):
    name: str = Field(min_length=1, max_length=20, example='课程名字', title='课程名字')
    credit: float = Field(..., example='学分', title='学分')
    period: int = Field(..., example='课时', title='课时')


# 添加数据的JSON字段
class CourseCreate(CourseIn):
    id: str = Field(regex=r'^[1-9][0-9]{3}$', min_length=4, max_length=4, example='课程编号：1101', title='课程编号')


# 更新数据的JSON字段
class CourseUpdate(CourseIn):
    pass


# 查询数据的JSON字段
class CourseOut(CourseCreate):
    class Config:
        orm_mode = True  # 是否使用orm模型
