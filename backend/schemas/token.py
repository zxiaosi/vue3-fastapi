#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/24 14:48
# @Author : zxiaosi
# @desc : token
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """ token """
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """ 有效token """
    exp: Optional[str]  # 时间
    sub: Optional[int] = None
