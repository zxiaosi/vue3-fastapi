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
    data: SchemasType = None
    msg: str


def response(code: int = 200, data: Type[SchemasType] = None, msg: str = 'Success'):
    if code == 200:
        logger.info(msg)
    elif code == 404:
        logger.error(msg)
    else:
        logger.warning(msg)
    return {'code': code, 'data': data, 'msg': msg}
