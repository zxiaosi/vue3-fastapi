#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/22 17:17
# @Author : zxiaosi
# @desc : 日志接口
from fastapi import APIRouter

from common.depends import PageQuery, GetDB
from common.result import ResultSchema, Result
from common.route_log import LogRoute
from crud import sys_log_crud
from schemas import SysLogOut

router = APIRouter(route_class=LogRoute)


@router.get("/list")
async def root(db: GetDB, page: PageQuery) -> ResultSchema[list[SysLogOut]]:
    data = sys_log_crud.get_all(db, page)
    total = sys_log_crud.get_count(db)
    return Result.success(data=data, total=total)
