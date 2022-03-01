#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:03
# @Author : zxiaosi
# @desc : 操作专业表
from crud import CRUDBase
from models import Major
from schemas import MajorCreate, MajorUpdate


class CRUDMajor(CRUDBase[Major, MajorCreate, MajorUpdate]):
    pass


major = CRUDMajor(Major)
