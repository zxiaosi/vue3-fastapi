#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/6 1:23
# @Author : zxiaosi
# @desc : 用户角色表的模型
from pydantic import BaseModel, Field


class UserRoleIn(BaseModel):
    """ 共享数据模型 """
    user_id: int = Field(example='用户Id')
    role_id: int = Field(example='角色Id')


class UserRoleOut(UserRoleIn):
    """ 查询数据的数据模型 """
    id: int

    class Config:
        orm_mode = True  # 支持映射到ORM对象的模型
