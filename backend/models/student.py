#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 13:48
# @Author : 小四先生
# @desc : 学生表
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, ForeignKey, CheckConstraint, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .major import Major  # noqa


class Student(Base):
    """ 学生表 """
    id = Column(String(10),
                primary_key=True,
                index=True,
                doc='学号')

    name = Column(String(10),
                  nullable=False,
                  index=True,
                  doc='学生姓名')

    sex = Column(String(5),
                 CheckConstraint("sex in ('man', 'woman')"),
                 nullable=False,
                 doc='学生性别')

    birthday = Column(Date,
                      default=date(2012, 1, 1),
                      nullable=False,
                      doc='学生生日')

    hashed_password = Column(String(60), nullable=True, doc='学生密码')

    major_id = Column(String(6), ForeignKey('major.id'), doc='专业编号')

    major = relationship("Major", backref="student")
