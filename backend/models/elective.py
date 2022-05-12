#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 选课表
from sqlalchemy import Column, ForeignKey, Integer

from models import Base


class Elective(Base):
    """ 选课表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    grade = Column(Integer, default=0, server_default='0', comment='成绩')

    studentId = Column(Integer, ForeignKey('student.id', ondelete='CASCADE'), nullable=False, comment='学号')

    courseId = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'), nullable=False, comment='课程编号')
