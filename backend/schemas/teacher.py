#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 10:01
# @Author : zxiaosi
# @desc : 教师表模型
from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel, Field

from schemas import GMT


class TeacherIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(min_length=1, max_length=10, example='姓名')
    sex: Literal['0', '1'] = Field(..., example='性别: 0->男, 1->女')
    birthday: date = Field(..., example='生日: 1998-7-2')
    education: Literal['1', '2', '3'] = Field(..., example='学历：1->学士, 2->硕士, 3->博士')
    title: Literal['1', '2', '3', '4'] = Field(..., example='职称：1->助教, 2->讲师, 3->副教授, 4->教授')
    image: str = Field(example='头像')
    address: str = Field(example='地址')
    departmentId: str = Field(regex=r'^10[0-9]{2}$', min_length=4, max_length=4, example='院系编号')


class TeacherUpdate(TeacherIn):
    """ 更新数据的字段验证 """
    password: Optional[str] = Field(max_length=60, example='密码')  # 前端返回可不带该字段


class TeacherCreate(TeacherUpdate):
    """ 添加数据时的字段验证 """
    id: str = Field(regex=r'^[1-9][0-9]{5}$', min_length=6, max_length=6, example='职工号：180404')


class TeacherOut(TeacherIn, GMT):
    """ 查询数据的字段验证 """
    id: int = Field(..., example='职工号：180404')
    departmentId: int = Field(..., example='院系编号')

    class Config:
        orm_mode = True  # 是否使用orm模型(结果为字典类型)
