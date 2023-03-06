#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/30 18:47
# @Author : zxiaosi
# @desc : 响应的数据模型与数据结构
from typing import Any, TypeVar, Generic

from pydantic.generics import GenericModel

T = TypeVar("T")  # 泛型 T ：https://docs.pydantic.dev/usage/models/#generic-models


class ResultSchema(GenericModel, Generic[T]):
    """ 结果数据模型 """
    code: int
    data: T | list[T] | None
    total: int | None
    msg: str | None


class Result:
    """ 结果数据结构 """

    @staticmethod
    def success(*, code: int = 0, data: T = None, total: int = 0, msg: str = "Success") -> ResultSchema[T]:
        """ 成功响应数据结构 """
        return ResultSchema(code=code, data=data, total=total, msg=msg)

    @staticmethod
    def fail(*, code: int = 1, data: Any = None, msg: str = "Fail") -> ResultSchema[T]:
        """ 失败响应数据结构 """
        return ResultSchema(code=code, data=data, msg=msg, total=None)
