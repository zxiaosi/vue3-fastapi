#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 教师表
from datetime import date
from sqlalchemy import Column, String, ForeignKey, CheckConstraint, Date, Boolean, text, TIMESTAMP, func

from models import Base


class Teacher(Base):
    """ 教师表 """
    id = Column(String(6), primary_key=True, index=True, comment='职工号')

    name = Column(String(10), unique=True, nullable=False, comment='姓名')

    sex = Column(String(5), CheckConstraint("sex in ('man', 'woman')"), server_default=text("'man'"), comment='性别')

    birthday = Column(Date, default=date(2012, 1, 1), nullable=False, comment='生日')

    hashed_password = Column(String(60), nullable=False, comment='密码')

    education = Column(String(8),
                       CheckConstraint("education in ('Bachelor', 'Master', 'Doctor')"),
                       server_default=text("'Bachelor'"),
                       comment='学历')

    title = Column(String(9),
                   CheckConstraint("title in ('Assistant', 'Lecturer', 'Associate', 'Professor')"),
                   server_default=text("'Assistant'"),
                   comment='职称')

    is_active = Column(Boolean(), server_default=text("True"), comment='是否登录')

    department_id = Column(String(4), ForeignKey('department.id', ondelete='CASCADE'), doc='院系编号')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
