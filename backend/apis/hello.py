#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 11:04
# @Author : zxiaosi
# @desc : 默认接口
from fastapi import APIRouter

from common import LogRoute, ResultSchema, Result

router = APIRouter(route_class=LogRoute)


@router.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@router.get("/lang/list")
def language_list() -> ResultSchema[dict]:
    return Result.success(data={
        "2022-01": 2, "2022-02": 8, "2022-03": 5, "2022-04": 5, "2022-05": 6, "2022-06": 10, "2022-07": 1, "2022-08": 2,
        "2022-09": 0, "2022-10": 5, "2022-11": 8, "2022-12": 2, "2023-01": 0, "2023-02": 4, "2023-03": 7
    })
