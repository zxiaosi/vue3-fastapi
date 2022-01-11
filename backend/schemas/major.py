#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:00
# @Author : zxiaosi
# @desc : JSON字段验证[专业表]
from typing import Optional
from pydantic import BaseModel, Field


# id 为 str 为了能够使用正则表达式匹配
# ... 表示必填, 和max_length冲突, 使用max_length可以输入空值
# Optional[str]: union[str, None] --> 表示 数据可以为str类型或者为空

# 共享JSON字段
class MajorIn(BaseModel):
    name: str = Field(max_length=20, example='专业名字', title='专业名字')
    assistant: str = Field(min_length=1, max_length=10, example='辅导员名', title='辅导员名')
    phone: Optional[str] = Field(regex=r'(^\s{0}$)|^(0\d{2,3}-\d{7,8})|(1[34578]\d{9})$',  # 匹配 '' || 手机号
                                 max_length=11, example='辅导员手机号', title='辅导员手机号')
    department_id: str = Field(regex=r'^10[0-9]{2}$', min_length=4, max_length=4,
                               example='院系编号', title='院系编号')


# 添加数据的JSON字段
class MajorCreate(MajorIn):
    id: str = Field(regex=r'^10[0-9]{4}$', min_length=6, max_length=6, example='专业编号', title='专业编号')


# 更新数据的JSON字段
class MajorUpdate(MajorIn):
    pass


# 查询数据的JSON字段
class MajorOut(MajorCreate):
    class Config:
        orm_mode = True  # 是否使用orm模型
