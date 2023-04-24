#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/4/23 17:12
# @Author : zxiaosi
# @desc : 角色表模型
from pydantic import BaseModel, Field

from schemas.gmt import GMT


class RoleIn(BaseModel):
    """ 共享数据模型 """
    name: str = Field(example='角色名称')
    code: str = Field(example='角色code')
    description: str | None = Field(example='角色描述')


class RoleOut(RoleIn, GMT):
    """ 查询数据的数据模型 """
    id: int
    is_deleted: int

    class Config:
        orm_mode = True  # 支持映射到ORM对象的模型
