#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/8 13:48
# @Author : zxiaosi
# @desc : 自定义异常
class IdNotExist(Exception):
    """ 查询id不存在 """

    def __init__(self, err_desc: str = "查询id不存在"):
        self.err_desc = err_desc
