#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/1 16:07
# @Author : zxiaosi
# @desc : 自定义异常
from starlette import status


class CustomException(Exception):
    """ 自定义异常 """

    def __init__(self, code: int, err_desc: str = ""):
        self.code = code
        self.err_desc = err_desc


class DuplicateRequests(CustomException):
    """ 重复请求 """

    def __init__(self, code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, err_desc: str = "请勿重复提交"):
        super().__init__(code=code, err_desc=err_desc)


class WrongPublicKey(CustomException):
    """ 错误的公钥 """

    def __init__(self, code: int = status.HTTP_401_UNAUTHORIZED, err_desc: str = "密码解密错误"):
        super().__init__(code=code, err_desc=err_desc)


class BadCredentials(CustomException):
    """ 错误的凭证 """

    def __init__(self, code: int = status.HTTP_401_UNAUTHORIZED, err_desc: str = "用户登录信息已失效"):
        super().__init__(code=code, err_desc=err_desc)


class UserErrors(CustomException):
    """ 用户相关错误集合 """

    def __init__(self, code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, err_desc: str = ""):
        super().__init__(code=code, err_desc=err_desc)
