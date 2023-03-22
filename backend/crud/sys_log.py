#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/22 16:39
# @Author : zxiaosi
# @desc : 日志表的增删改查
from crud.base import CRUDBase
from models import SysLog
from schemas import SysLogIn


class CRUDUserRole(CRUDBase[SysLog, SysLogIn, SysLogIn]):
    pass


sys_log_crud = CRUDUserRole(SysLog)
