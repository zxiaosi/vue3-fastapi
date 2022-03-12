#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/3/9 11:19
# @Author : zxiaosi
# @desc : 权限表
from sqlalchemy import Column, Integer, String, CheckConstraint

from models import Base


class Permission(Base):
    """ 权限表 """
    code = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='权限码')

    name = Column(String(10), comment='权限名称')

    desc = Column(String(20), comment='权限描述')
