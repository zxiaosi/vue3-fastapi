#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023-05-18 16:18
# @Author : zxiaosi
# @desc : 角色接口
from fastapi import APIRouter

from common.depends import GetDB, PageQuery
from common.result import Result, ResultSchema
from common.route_log import LogRoute
from crud import role_crud
from schemas import RoleOut

router = APIRouter(route_class=LogRoute)


@router.get("/list")
def roles(db: GetDB, page: PageQuery, name: str | None = None) -> ResultSchema[list[RoleOut]]:
    """ 角色列表 """
    role_obj = role_crud.get_all(db=db, page=page, name=name)
    total = role_crud.get_count(db=db)
    return Result.success(data=role_obj, total=total)
