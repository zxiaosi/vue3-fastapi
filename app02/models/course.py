#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 课程表
from sqlalchemy import Column, String, Float, SmallInteger

from app02.db.base_class import Base


class Course(Base):
    course_id = Column(String(6),
                       primary_key=True,
                       index=True,
                       doc='课程编号')

    course_name = Column(String(20),
                         nullable=False,
                         index=True,
                         doc='课程名字')

    course_credit = Column(Float,
                           nullable=False,
                           doc='学分')

    course_period = Column(SmallInteger,
                           nullable=False,
                           doc='课时')
