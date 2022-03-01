#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : zxiaosi
# @desc : 专业表
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, func

from models import Base


class Major(Base):
    """ 专业表 """
    id = Column(String(6), primary_key=True, index=True, comment='编号')

    name = Column(String(20), unique=True, nullable=False, comment='名字')

    assistant = Column(String(10), nullable=False, comment='辅导员姓名')

    phone = Column(String(11), comment='辅导员手机号')

    department_id = Column(String(4), ForeignKey('department.id', ondelete='CASCADE'), comment='院系编号')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
