#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/28 13:46
# @Author : zxiaosi
# @desc : 页码模型
from pydantic import BaseModel


class PageSchema(BaseModel):
    """ 分页查询参数 """
    page: int = 1
    page_size: int = 10
