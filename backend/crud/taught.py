#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/5/10 21:00
# @Author : zxiaosi
# @desc : 操作讲授表
from crud import CRUDBase
from models import Taught
from schemas import TaughtCreate, TaughtUpdate


class CRUDTaught(CRUDBase[Taught, TaughtCreate, TaughtUpdate]):
    pass


taught = CRUDTaught(Taught)
