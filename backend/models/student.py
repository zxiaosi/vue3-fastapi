#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 13:48
# @Author : zxiaosi
# @desc : 学生表
from datetime import date

from sqlalchemy import Column, Integer, String, Date, text, ForeignKey
from sqlalchemy.orm import relationship

from core import settings, get_password_hash
from models import Base
from utils import check_or_enum


class Student(Base):
    """ 学生表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='学号')

    name = Column(String(10), unique=False, nullable=False, comment='姓名')

    sex = check_or_enum(name='sex', enumList=['0', '1'], comment='性别: 0->男, 1->女')

    birthday = Column(Date, default=date(2012, 1, 1), comment='生日')

    address = Column(String(20), server_default=text("'广东省广州市'"), comment='地址')

    image = Column(String(60), server_default=f'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg', comment='头像')

    hashed_password = Column(String(60), server_default=get_password_hash('123456'), comment='密码')

    majorId = Column(Integer, ForeignKey('major.id', ondelete='CASCADE'), nullable=False, comment='专业编号')

    elective = relationship('Elective')  # 不是字段, 可以通过 student ORM对象引用 elective 表的类集合
