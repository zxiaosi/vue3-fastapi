#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 选课表
from sqlalchemy import Column, String, ForeignKey, Integer, text
from sqlalchemy.orm import relationship, backref

from db.base_class import Base


class SelectCourse(Base):
    """ 选课表 """
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, doc='编号')

    grade = Column(Integer, default=0, server_default=text('0'), doc='成绩')

    student_id = Column(String(10), ForeignKey('student.id'), doc='学号')

    student = relationship("Student", backref=backref("selectCourse", cascade="all, delete"))

    teacher_id = Column(String(6), ForeignKey('teacher.id'), doc='职工号')

    teacher = relationship("Teacher", backref=backref("selectCourse", cascade="all, delete"))

    course_id = Column(Integer, ForeignKey('course.id'), doc='课程编号')

    course = relationship("Course", backref=backref("selectCourse", cascade="all, delete"))
