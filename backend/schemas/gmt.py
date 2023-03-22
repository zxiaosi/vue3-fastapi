#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 18:44
# @Author : zxiaosi
# @desc : 常用模型
from datetime import datetime

from pydantic import BaseModel, validator


class GMT(BaseModel):
    """ 时间字段处理 """
    create_time: datetime
    update_time: datetime

    @validator("create_time", "update_time")
    def format_time(cls, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间


class QuerySchema(BaseModel):
    """ 分页查询参数 """
    page: int = 1
    page_size: int = 10
    q: str | None = None


class OrderSchema(BaseModel):
    """ 排序参数 """
    field: str | None = "id"
    type: str = "desc"
