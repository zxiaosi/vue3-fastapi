#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/2/24 11:20
# @Author : zxiaosi
# @desc : 待办模型
from typing import Optional

from pydantic import BaseModel


class TodoId(BaseModel):
    id: Optional[int]


class Todo(BaseModel):
    title: Optional[str]
    status: Optional[bool] = False
