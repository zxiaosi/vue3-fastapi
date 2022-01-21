#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/13 13:41
# @Author : zxiaosi
# @desc : 封装 统一的JSON格式
from typing import Type, Union
from starlette import status
from starlette.responses import Response
from fastapi.responses import ORJSONResponse

from schemas.result import SchemasType
from utils import logger


# 因为 data 数据要符合 SchemasType 模型，不符合JSONResponse的序列化
def resp_200(*, data: Union[Type[SchemasType], dict] = None, msg: str = "Success"):
    logger.info(msg)
    return {'code': 200, 'data': data, 'msg': msg}


def resp_400(code: int = 400, data: str = None, msg: str = "BAD REQUEST") -> Response:
    return ORJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'code': code, 'msg': msg, 'data': data})


def resp_403(*, data: str = None, msg: str = "Forbidden") -> Response:
    return ORJSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={'code': 403, 'msg': msg, 'data': data})


def resp_404(*, data: str = None, msg: str = "Page Not Found") -> Response:
    return ORJSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'code': 404, 'msg': msg, 'data': data})


def resp_422(*, data: str = None, msg: Union[list, dict, str] = "UNPROCESSABLE_ENTITY") -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'code': 422, 'msg': msg, 'data': data}
    )


def resp_500(*, data: str = None, msg: Union[list, dict, str] = "Server Internal Error") -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={'code': 500, 'msg': msg, 'data': data}
    )
