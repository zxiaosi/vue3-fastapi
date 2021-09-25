#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 选课表
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import relationship

from app02.db.base_class import Base

if TYPE_CHECKING:
    from .student import Student  # noqa
    from .teacher import Teacher  # noqa
    from .course import Course  # noqa


class SelectCourse(Base):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                index=True,
                doc='编号')

    grade = Column(SmallInteger,
                   default='',
                   doc='成绩')

    student_id = Column(String(10),
                        ForeignKey('student.student_id'),
                        nullable=True,
                        doc='学号')

    student = relationship("Student", backref="selectCourse")

    teacher_id = Column(String(10),
                        ForeignKey('teacher.teacher_id'),
                        nullable=True,
                        doc='职工号')

    teacher = relationship("Teacher", backref="selectCourse")

    course_id = Column(String(6),
                       ForeignKey('course.course_id'),
                       nullable=True,
                       doc='课程编号')

    course = relationship("Course", backref="selectCourse")
