#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 13:48
# @Author : 小四先生
# @desc : 学生表
from sqlalchemy import Column, String, ForeignKey, CheckConstraint, DateTime, text
from sqlalchemy.orm import relationship

from app02.db.base_class import Base


class Student(Base):
    student_id = Column(String(10),
                        primary_key=True,
                        index=True,
                        doc='学号')

    student_name = Column(String(10),
                          nullable=False,
                          index=True,
                          doc='学生姓名')

    student_sex = Column(String(2),
                         CheckConstraint("student_sex in ('男', '女')"),
                         nullable=False,
                         doc='学生性别')

    student_birthday = Column(DateTime,
                              server_default=text('CURRENT_TIMESTAMP'),
                              nullable=False,
                              doc='学生生日')

    student_password = Column(String(20), nullable=True, doc='学生密码')

    major_id = Column(String(6), ForeignKey('major.major_id'), doc='专业编号')

    major = relationship("Major", back_populates="student_fk_major")
