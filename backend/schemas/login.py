#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/2/25 11:23
# @Author : zxiaosi
# @desc : 登录模型
from pydantic import BaseModel


class Login(BaseModel):
    """ 登录模型 """
    username: str
    password: str
