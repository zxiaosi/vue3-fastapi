#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023-05-18 16:39
# @Author : zxiaosi
# @desc : 资源接口
from fastapi import APIRouter

from common.depends import GetDB, PageQuery
from common.result import Result, ResultSchema
from common.route_log import LogRoute
from crud import resource_crud
from schemas import ResourceOut

router = APIRouter(route_class=LogRoute)


@router.get("/list")
def resources(db: GetDB, page: PageQuery, name: str | None = None) -> ResultSchema[list[ResourceOut]]:
    """ 资源列表 """
    resource_obj = resource_crud.get_all(db=db, page=page, name=name)
    total = resource_crud.get_count(db=db)
    return Result.success(data=resource_obj, total=total)
