#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 18:43
# @Author : zxiaosi
# @desc : 资源表模型
from pydantic import BaseModel, Field

from schemas.gmt import GMT


class ResourceIn(BaseModel):
    """ 共享数据模型 """
    name: str = Field(example='资源名称')
    level: int | None = Field(default=0, ge=0, le=2, example='层级: 0 目录 1 菜单 2 权限')
    pid: int | None = Field(default=0, ge=0, example='父节点id')
    icon: str | None = Field(example="图标")
    menu_url: str | None = Field(example='页面路由')
    request_url: str | None = Field(example='请求url')
    permission_code: str | None = Field(example='权限code')


class ResourceCreate(ResourceIn):
    """ 添加数据时的数据模型 """
    pass


class ResourceUpdate(ResourceCreate):
    """ 更新数据的数据模型 """
    pass


class ResourceOut(ResourceIn, GMT):
    """ 查询数据的数据模型 """
    id: int
    is_deleted: int

    class Config:
        orm_mode = True  # 支持映射到ORM对象的模型


class MenuOut(BaseModel):
    """ 查询数据的数据模型 """
    id: int
    name: str = Field(example='资源名称')
    icon: str | None = Field(example="图标")
    menu_url: str | None = Field(example='页面路由')
    children: list['MenuOut'] | None = Field(default=[])

    class Config:
        orm_mode = True  # 支持映射到ORM对象的模型
