#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 选课表
from sqlalchemy import Column, String, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import relationship

from app02.db.base_class import Base


class SelectCourse(Base):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                index=True,
                doc='编号')

    grade = Column(SmallInteger,
                   default='',
                   doc='成绩')

    stu_id = Column(String(10),
                    ForeignKey('student.student_id'),
                    nullable=True,
                    doc='学号')

    student = relationship("Student", back_populates="selectCourse_fk_student")

    teach_id = Column(String(10),
                      ForeignKey('teacher.teacher_id'),
                      nullable=True,
                      doc='职工号')

    teacher = relationship("Teacher", back_populates="selectCourse_fk_teacher")

    course_id = Column(String(6),
                       ForeignKey('course.course_id'),
                       nullable=True,
                       doc='课程编号')

    course = relationship("Course", back_populates="selectCourse_fk_course")
