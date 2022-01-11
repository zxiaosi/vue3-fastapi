#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 课程表
from sqlalchemy import Column, String, Float, SmallInteger, text, Integer

from db.base_class import Base


class Course(Base):
    """ 课程表 """
    id = Column(Integer, primary_key=True, index=True, doc='课程编号')

    name = Column(String(20), unique=True, nullable=False, doc='课程名字')

    credit = Column(Float, default=0, server_default=text('0'), doc='学分')

    period = Column(SmallInteger, default=0, server_default=text('0'), doc='课时')
