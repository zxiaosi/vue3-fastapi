#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/13 13:41
# @Author : 小四先生
# @desc : 封装 统一的JSON格式
from typing import TypeVar, Generic, Type

from pydantic.generics import GenericModel
from utils.logger import logger

SchemasType = TypeVar("SchemasType")


class RestfulModel(GenericModel, Generic[SchemasType]):
    code: int
    msg: str
    data: SchemasType = None


def response(code: int = 200, msg: str = 'Success', data: Type[SchemasType] = None):
    if code == 200:
        logger.info(msg)
    else:
        logger.warning(msg)
    return {'code': code, 'msg': msg, 'data': data}
