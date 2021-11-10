#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/10 15:32
# @Author : 小四先生
# @desc : 返回的消息
from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
