#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 讲授表
from sqlalchemy import Column, ForeignKey, Integer

from models import Base


class Taught(Base):
    """ 讲授表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    teacherId = Column(Integer, ForeignKey('teacher.id', ondelete='CASCADE'), comment='职工号')

    courseId = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'), comment='课程编号')
