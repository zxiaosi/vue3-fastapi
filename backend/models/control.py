#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 控制表
from sqlalchemy import Column, Integer, String, CheckConstraint

from backend.db.base_class import Base


class Control(Base):
    """ 控制表 """
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                doc='编号')

    if_take_Course = Column(String(1),
                            CheckConstraint("if_take_Course in ('0', '1')"),
                            nullable=False,
                            doc='选课控制')

    if_input_Grade = Column(String(1),
                            CheckConstraint("if_input_Grade in ('0', '1')"),
                            nullable=False,
                            doc='成绩录入控制')
