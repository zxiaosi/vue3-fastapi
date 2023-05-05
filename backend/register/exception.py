#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 10:05
# @Author : zxiaosi
# @desc : 全局异常捕获
import traceback

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from redis.exceptions import RedisError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from common.custom_exc import CustomException
from common.custom_log import my_logger
from common.result import ResultSchema, Result
from common.route_log import get_request_params

"""
    {
      "headers": "xxx", # 请求头
      "status_code": 200, # HTTP通讯状态, eg: 401、403、500
      "content": { # 自定义内容, eg: Result.success | Result.fail
        "code": 0, # 自定义状态码, 方便前端判断. 为了区别 HTTP通讯状态, 常规定 0 | 1.
        "data": T, # 数据
        "msg": "xxx"
      }
    }
"""


def response_body(
        request: Request,
        content: ResultSchema,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
) -> JSONResponse:
    """ 返回响应体 """

    response = {
        "content": content,
        "status_code": status_code,
        "headers": {  # 解决跨域问题(仿照500错误的响应头)
            "access-control-allow-origin": request.headers.get("origin") or '*',
            "access-control-allow-credentials": "true",
            "content-type": "application/json",
            "vary": "Origin",
        }
    }

    return JSONResponse(**jsonable_encoder(response))


def register_exception(app: FastAPI):
    """
        全局异常捕获 -- https://fastapi.tiangolo.com/tutorial/handling-errors/
        starlette 服务器在返回500时删除了请求头信息, 从而导致了cors跨域问题, 前端无法获取到响应头信息
        详见: https://github.com/encode/starlette/issues/1175#issuecomment-1225519424
    """

    @app.exception_handler(CustomException)
    async def error_user_handler(request: Request, exc: CustomException) -> JSONResponse:
        """ 自定义异常 """
        my_logger.error(f"自定义异常: URL:{request.url}\nHeaders:{request.headers}\nException:{exc.err_desc}.")
        if exc.code == status.HTTP_401_UNAUTHORIZED:
            return JSONResponse(status_code=exc.code, content=Result.fail(msg=exc.err_desc).dict())
        else:
            return response_body(request=request, content=Result.fail(msg=exc.err_desc), status_code=exc.code)

    @app.exception_handler(RedisError)
    async def validation_exception_handler(request: Request, exc: RedisError) -> JSONResponse:
        """ 系统异常 -- Redis错误 """
        my_logger.error(f"Redis错误: URL:{request.url}\nHeaders:{request.headers}\nException:{exc}.")
        return response_body(request=request, content=Result.fail(msg="Redis错误!"))

    @app.exception_handler(SQLAlchemyError)
    async def validation_exception_handler(request: Request, exc: SQLAlchemyError) -> JSONResponse:
        """ 系统异常 -- SQLAlchemy错误 """
        my_logger.error(f"SQL语法错误: URL:{request.url}\nHeaders:{request.headers}\nException:{exc}.")
        return response_body(request=request, content=Result.fail(msg="SQL语法错误!"))

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """ HTTP通信错误 -- 请求参数验证错误 """
        params = await get_request_params(request)
        my_logger.error(f"请求参数验证错误: URL:{request.url}, Params:{params}\nHeaders:{request.headers}\n"
                        f"Exception:{jsonable_encoder(exc.errors())}.")

        content = Result.fail(msg="请求参数异常!").dict()
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=content)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
        """ HTTP通信错误(未进到接口里面) """
        my_logger.error(f"HTTP通讯错误: URL:{request.url}\nHeaders:{request.headers} \nException:{repr(exc)}.")
        return response_body(request=request, content=Result.fail(msg=exc.detail), status_code=exc.status_code)

    @app.exception_handler(Exception)
    async def http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        """ 全局异常 """
        my_logger.error(f"全局异常: URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_body(request=request, content=Result.fail(msg="未知错误！"))
