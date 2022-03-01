#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : zxiaosi
# @desc : 院系表
from sqlalchemy import Column, String, TIMESTAMP, func

from models import Base


class Department(Base):
    """ 院系表 """
    id = Column(String(4), primary_key=True, index=True, comment='编号')

    name = Column(String(20), unique=True, nullable=False, comment='名字')

    chairman = Column(String(10), nullable=False, comment='主任姓名')

    phone = Column(String(11), comment='主任手机号')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
