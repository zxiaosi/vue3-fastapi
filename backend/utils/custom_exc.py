#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 13:48
# @Author : zxiaosi
# @desc : 自定义异常
class IpError(Exception):
    """ ip错误 """

    def __init__(self, err_desc: str = "ip错误"):
        self.err_desc = err_desc


class SetRedis(Exception):
    """ Redis存储失败 """

    def __init__(self, err_desc: str = "Redis存储失败"):
        self.err_desc = err_desc


class IdNotExist(Exception):
    """ 查询id不存在 """

    def __init__(self, err_desc: str = "查询id不存在"):
        self.err_desc = err_desc


class UserNotExist(Exception):
    """ 用户不存在 """

    def __init__(self, err_desc: str = "用户不存在"):
        self.err_desc = err_desc


class AccessTokenFail(Exception):
    """ 访问令牌失败 """

    def __init__(self, err_desc: str = "访问令牌失败"):
        self.err_desc = err_desc


class ErrorUser(Exception):
    """ 错误的用户名或密码 """

    def __init__(self, err_desc: str = "错误的用户名或密码"):
        self.err_desc = err_desc


class PermissionNotEnough(Exception):
    """ 权限不足,拒绝访问 """

    def __init__(self, err_desc: str = "权限不足,拒绝访问"):
        self.err_desc = err_desc
