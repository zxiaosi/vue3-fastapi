#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 11:24
# @Author : zxiaosi
# @desc : 对返回数据验证
from typing import TypeVar, Generic, Optional
from pydantic.generics import GenericModel

SchemasType = TypeVar("SchemasType")


# Optional[str]: union[str, None] --> 表示 数据可以为str类型或者为空

# 普通结果验证
class ResultModel(GenericModel, Generic[SchemasType]):
    """ 普通结果验证 """
    code: int
    data: SchemasType
    msg: Optional[str]


# 自定义结果 --> data 数据
class ResultPlus(GenericModel, Generic[SchemasType]):
    dataList: SchemasType
    count: int


# 自定义结果验证
class ResultPlusModel(GenericModel, Generic[SchemasType]):
    """ 自定义结果验证 """
    code: int
    data: ResultPlus[SchemasType]
    msg: Optional[str]
