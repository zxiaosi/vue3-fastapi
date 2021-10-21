#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 课程表
from sqlalchemy import Column, String, Float, SmallInteger

from db.base_class import Base


class Course(Base):
    """ 课程表 """
    id = Column(String(4),
                primary_key=True,
                index=True,
                doc='课程编号')

    name = Column(String(20),
                  nullable=False,
                  index=True,
                  doc='课程名字')

    credit = Column(Float, nullable=False, doc='学分')

    period = Column(SmallInteger, nullable=False, doc='课时')
