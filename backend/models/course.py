#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 课程表
from sqlalchemy import Column, String, Float, SmallInteger, text, TIMESTAMP, func

from models import Base


class Course(Base):
    """ 课程表 """
    id = Column(String(4), primary_key=True, index=True, comment='编号')

    name = Column(String(20), unique=True, nullable=False, comment='名字')

    credit = Column(Float, default=0, server_default=text('0'), comment='学分')

    period = Column(SmallInteger, default=0, server_default=text('0'), comment='课时')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
