#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 11:24
# @Author : zxiaosi
# @desc : 返回数据验证
from typing import TypeVar, Generic, Optional, Union
from pydantic import BaseModel
from pydantic.generics import GenericModel

SchemasType = TypeVar("SchemasType", bound=BaseModel)


class ResultModel(GenericModel, Generic[SchemasType]):
    """ 普通结果验证 """
    code: int
    data: Union[SchemasType, str, list, dict, bool]
    msg: Optional[str]


class ResultPlus(GenericModel, Generic[SchemasType]):
    """ 自定义结果 --> data 数据 """
    dataList: SchemasType
    count: int


class ResultPlusModel(GenericModel, Generic[SchemasType]):
    """ 自定义结果验证 """
    code: int
    data: ResultPlus
    msg: Optional[str]
