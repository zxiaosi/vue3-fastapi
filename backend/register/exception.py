#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 15:48
# @Author : zxiaosi
# @desc :
import json
import traceback

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from starlette.requests import Request

from utils import logger, resp_400, resp_500, resp_422
from utils.custom_exc import IdNotExist


def register_exception(app: FastAPI):
    """
    全局异常捕获
    注意 别手误多敲一个s
    exception_handler
    exception_handlers
    两者有区别
        如果只捕获一个异常 启动会报错
        @exception_handlers(UserNotFound)
    TypeError: 'dict' object is not callable
    :param app:
    :return:
    """

    # 自定义异常 捕获

    # 查询id不存在
    @app.exception_handler(IdNotExist)
    async def id_not_exist_handler(request: Request, exc: IdNotExist):
        """ 查询id不存在 """
        logger.warning(f"{exc.err_desc}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        return resp_400(msg=exc.err_desc)

    # 内部参数验证异常
    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, exc: ValidationError):
        """ 内部参数验证异常 """
        logger.error(f"内部参数验证错误\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{exc.errors()}")
        return resp_500(msg=exc.errors())

    # 请求参数验证异常
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """ 请求参数验证异常 """
        logger.error(f"请求参数格式错误\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{exc.errors()}")
        return resp_422(msg=exc.errors())

    # 添加的值与数据库中数据冲突(MySQL报错返回会携带错误码(1062, 1452), Sqlite报错只有报错内容)
    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request: Request, exc: IntegrityError):
        """ 添加数据的值与数据冲突 """
        code: str = str(exc.orig)[1:5]  # 1062(唯一) || 1452(外键)
        if code == "1062":  # 添加的值与数据库中已存在(主键、唯一索引)
            text: str = f"添加数据的 id-{exc.params[0]} 或 name-{exc.params[1]} 已存在, 添加失败!"
        # elif code == "1452" and request.method == "POST":  # 添加的值数据库中不存在(外键)
        #     text: str = f"添加数据的 外键-{exc.params[-1]} 不存在, 添加失败!"
        # elif code == "1452" and request.method == "PUT":  # 更新的值数据库中不存在(外键)
        #     text: str = f"更新数据的 外键-{exc.params[-2]} 不存在, 添加失败!"
        elif code == "1452" and request.method == "POST":  # 添加的值数据库中不存在(外键)
            text: str = f"添加数据的外键不存在, 添加失败!"
        elif code == "1452" and request.method == "PUT":  # 更新的值数据库中不存在(外键)
            text: str = f"更新数据的外键不存在, 添加失败!"
        else:
            text: str = f"添加数据的值与数据库中数据冲突, 添加失败!"
        logger.warning(f"{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{exc.orig}")
        return resp_400(msg=text)

    # 删除数据的id在数据库中不存在
    @app.exception_handler(UnmappedInstanceError)
    async def un_mapped_instance_error_handler(request: Request, exc: UnmappedInstanceError):
        """ 删除数据的id在数据库中不存在 """
        id: int = request.path_params.get("id")
        text: str = f"不存在编号为 {id} 的数据, 删除失败!"
        logger.warning(f"{text}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        return resp_400(msg=text)

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """ 全局所有异常 """
        logger.error(f"全局异常\n{request.method}URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return resp_500(msg="服务器内部错误")
