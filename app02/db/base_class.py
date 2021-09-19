#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:14
# @Author : 小四先生
# @desc : 封装 创建表名 的函数
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # 自动生成表名 __tablename__
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
