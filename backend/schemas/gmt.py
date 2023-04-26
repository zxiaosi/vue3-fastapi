#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 18:44
# @Author : zxiaosi
# @desc : 时间模型
from datetime import datetime

from pydantic import BaseModel, validator


class GMT(BaseModel):
    """ 时间字段处理 """
    create_time: datetime | None
    update_time: datetime | None

    @validator("create_time", "update_time")
    def format_time(cls, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间
