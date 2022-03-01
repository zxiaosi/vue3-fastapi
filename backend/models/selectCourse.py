#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 选课表
from sqlalchemy import Column, String, ForeignKey, Integer, text, func, TIMESTAMP

from models import Base


class SelectCourse(Base):
    """ 选课表 """
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    grade = Column(Integer, default=0, server_default=text('0'), comment='成绩')

    student_id = Column(String(10), ForeignKey('student.id', ondelete='CASCADE'), comment='学号')

    teacher_id = Column(String(6), ForeignKey('teacher.id', ondelete='CASCADE'), comment='职工号')

    course_id = Column(String(4), ForeignKey('course.id', ondelete='CASCADE'), comment='课程编号')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
