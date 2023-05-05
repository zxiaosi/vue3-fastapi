#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 11:04
# @Author : zxiaosi
# @desc : 默认接口
from fastapi import APIRouter

from common.route_log import LogRoute

router = APIRouter(route_class=LogRoute)


@router.get("/")
async def root() -> dict:
    return {"message": "Hello World"}
