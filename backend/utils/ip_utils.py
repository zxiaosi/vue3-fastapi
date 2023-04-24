#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/4/18 17:56
# @Author : zxiaosi
# @desc : ip工具类
from starlette.requests import Request


class IPUtils:
    ip = "127.0.0.1"

    @classmethod
    def get_ip(cls, request: Request):
        if request.client.host:
            cls.ip = request.client.host

        if "X-FORWARDED-FOR" in request.headers:
            cls.ip = request.headers["X-FORWARDED-FOR"]

        if "X-Forwarded-For" in request.headers:
            cls.ip = request.headers["X-Forwarded-For"]

        if "X-REAL-IP" in request.headers:
            cls.ip = request.headers["X-REAL-IP"]

        if "X-Real-IP" in request.headers:
            cls.ip = request.headers["X-Real-IP"]

        return cls.ip
