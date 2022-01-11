#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 教师表
from datetime import date
from sqlalchemy import Column, String, ForeignKey, CheckConstraint, Date, Boolean, text
from sqlalchemy.orm import relationship, backref

from db.base_class import Base


class Teacher(Base):
    """ 教师表 """
    id = Column(String(6), primary_key=True, index=True, doc='职工号')

    name = Column(String(10), unique=True, nullable=False, doc='教师姓名')

    sex = Column(String(5),
                 CheckConstraint("sex in ('man', 'woman')"),
                 default='man',
                 server_default=text("'man'"),
                 doc='教师性别')

    birthday = Column(Date, default=date(2012, 1, 1), nullable=False, doc='教师生日')

    hashed_password = Column(String(60), nullable=False, doc='教师密码')

    education = Column(String(8),
                       CheckConstraint("education in ('Bachelor', 'Master', 'Doctor')"),
                       default='Bachelor',
                       server_default=text("'Bachelor'"),
                       doc='教师学历')

    title = Column(String(9),
                   CheckConstraint("title in ('Assistant', 'Lecturer', 'Associate', 'Professor')"),
                   default='Assistant',
                   server_default=text("'Assistant'"),
                   doc='教师职称')

    is_active = Column(Boolean(), default=True, doc='是否登录')

    department_id = Column(String(4), ForeignKey('department.id'), doc='院系编号')

    department = relationship("Department", backref=backref("teacher", cascade="all, delete"))
