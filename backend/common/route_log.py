#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/1 10:13
# @Author : zxiaosi
# @desc : 路由日志记录器
import time
from typing import Callable
from urllib.parse import parse_qsl

from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRoute
from redis_om import NotFoundError
from starlette.requests import Request
from starlette.responses import Response

from core.init_db import SessionLocal
from crud import sys_log_crud
from models import RequestIp, SysLog
from common.custom_log import my_logger
from common.custom_exc import DuplicateRequests
from utils.handle_date import get_current_time
from utils.handle_ip import IPUtils


# 详见: https://fastapi.tiangolo.com/advanced/custom-request-and-route/#custom-apiroute-class-in-a-router


class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            prevent_duplicate_requests(request)  # 防止重复请求

            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)

            await save_log(request, duration)  # 可以在这里将日志保存到数据库

            return response

        return custom_route_handler


def prevent_duplicate_requests(request: Request):
    """ 防止重复请求 (3秒内请求5次) """
    key = f"{request.client.host}+{request.get('path')}"
    try:
        request_obj = RequestIp.get(key)
        if request_obj.num >= 10:
            raise DuplicateRequests()
        else:
            RequestIp(num=request_obj.num + 1, pk=key).update()
    except NotFoundError:
        RequestIp(num=1, pk=key).save().expire(3)


async def get_request_params(request: Request) -> dict:
    """ 获取请求参数 """
    params: dict = {}  # 存储结果

    path_params = request.get("path_params")  # 路径参数
    if path_params:
        params.update(path_params)

    query_string = request.get("query_string")
    if query_string:
        query_params = parse_qsl(str(query_string, "utf-8"))  # 查询参数
        params.update(query_params)

    methods = ["POST", "PUT", "PATCH"]
    content_type = request.headers.get("content-type")
    if request.method in methods and "application/json" in content_type:
        body_params = await request.json()  # 请求体参数
        params.update(body_params)

    return params


async def save_log(request: Request, duration: float):
    """ 保存日志 """
    request_params = await get_request_params(request)
    sys_log = SysLog(url=request.get("path"), method=request.method, ip=IPUtils.get_ip(request), params=request_params,
                     spend_time=duration, create_time=get_current_time())

    my_logger.info(f"访问记录: {jsonable_encoder(sys_log)}.")

    if request.get("path") == "/api/log/list":  # 排除日志接口
        return

    with SessionLocal() as db:
        sys_log_crud.create(db, sys_log)
