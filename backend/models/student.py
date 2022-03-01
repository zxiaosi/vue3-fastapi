#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 13:48
# @Author : zxiaosi
# @desc : 学生表
from datetime import date
from sqlalchemy import Column, String, ForeignKey, CheckConstraint, Date, Boolean, text, TIMESTAMP, func

from models import Base


class Student(Base):
    """ 学生表 """
    id = Column(String(10), primary_key=True, index=True, comment='学号')

    name = Column(String(10), unique=False, nullable=False, comment='姓名')

    sex = Column(String(5), CheckConstraint("sex in ('man', 'woman')"), server_default=text("'man'"), comment='性别')

    birthday = Column(Date, default=date(2012, 1, 1), nullable=False, comment='生日')

    hashed_password = Column(String(60), nullable=False, comment='密码')

    is_active = Column(Boolean(), server_default=text("True"), comment='是否登录')

    major_id = Column(String(6), ForeignKey('major.id', ondelete='CASCADE'), comment='专业编号')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
