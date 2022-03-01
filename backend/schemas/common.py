#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/2/22 20:06
# @Author : zxiaosi
# @desc : 常用模型
from datetime import datetime

from pydantic import BaseModel, validator


class GMT(BaseModel):
    """ 时间字段处理 """
    gmt_create: datetime
    gmt_modify: datetime

    @validator("gmt_create", "gmt_modify")
    def parse_gmt(cls, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间


class Relation(BaseModel):
    """ 关系字段 """
    id: str
    name: str
