#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 选课表
from sqlalchemy import Column, ForeignKey, Integer, text

from models import Base


class SelectCourse(Base):
    """ 选课表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    grade = Column(Integer, default=0, server_default=text('0'), comment='成绩')

    student_id = Column(Integer, ForeignKey('student.id', ondelete='CASCADE'), comment='学号')

    teacher_id = Column(Integer, ForeignKey('teacher.id', ondelete='CASCADE'), comment='职工号')

    course_id = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'), comment='课程编号')
