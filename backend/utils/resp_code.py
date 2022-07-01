#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/13 13:41
# @Author : zxiaosi
# @desc : 响应状态码
from typing import Union, Any, Optional
from starlette import status
from starlette.responses import Response
from fastapi.responses import ORJSONResponse

from core.logger import logger


def resp_200(*, data: Any = '', msg: str = "Success") -> dict:
    logger.info(msg)
    return {'code': 200, 'data': data, 'msg': msg}


def resp_400(code: int = 400, data: str = None, msg: str = "请求错误(400)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'code': code, 'msg': msg, 'data': data})


def resp_401(*, data: str = None, msg: str = "未授权，请重新登录(401)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={'code': 401, 'msg': msg, 'data': data})


def resp_403(*, data: str = None, msg: str = "拒绝访问(403)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={'code': 403, 'msg': msg, 'data': data})


def resp_404(*, data: str = None, msg: str = "请求出错(404)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'code': 404, 'msg': msg, 'data': data})


def resp_422(*, data: str = None, msg: Union[list, dict, str] = "不可处理的实体") -> Response:
    return ORJSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                          content={'code': 422, 'msg': msg, 'data': data})


def resp_500(*, data: str = None, msg: Union[list, dict, str] = "服务器错误(500)") -> Response:
    return ORJSONResponse(headers={'Access-Control-Allow-Origin': '*'},
                          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          content={'code': 500, 'msg': msg, 'data': data})


def resp_502(*, data: str = None, msg: str = "网络错误(502)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content={'code': 502, 'msg': msg, 'data': data})


# ------------------------------------------- 以下不常用 -------------------------------------------

def resp_406(*, data: str = None, msg: str = "请求的格式不可得(406)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={'code': 406, 'msg': msg, 'data': data})


def resp_408(*, data: str = None, msg: str = "请求超时(408)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_408_REQUEST_TIMEOUT, content={'code': 408, 'msg': msg, 'data': data})


def resp_410(*, data: str = None, msg: str = "请求的资源被永久删除，且不会再得到的(410)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_410_GONE, content={'code': 410, 'msg': msg, 'data': data})


def resp_501(*, data: str = None, msg: str = "服务未实现(501)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content={'code': 501, 'msg': msg, 'data': data})


def resp_503(*, data: str = None, msg: str = "服务不可用(503)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                          content={'code': 503, 'msg': msg, 'data': data})


def resp_504(*, data: str = None, msg: str = "网络超时(504)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_504_GATEWAY_TIMEOUT, content={'code': 504, 'msg': msg, 'data': data})


def resp_505(*, data: str = None, msg: str = "HTTP版本不受支持(505)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED,
                          content={'code': 505, 'msg': msg, 'data': data})
