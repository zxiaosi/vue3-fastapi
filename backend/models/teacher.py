#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 教师表
from datetime import date
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from core import settings, get_password_hash
from models import Base
from utils import check_or_enum


class Teacher(Base):
    """ 教师表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='职工号')

    name = Column(String(10), unique=True, nullable=False, comment='姓名')

    sex = check_or_enum(name='sex', enumList=['0', '1'], comment='性别: 0->男, 1->女')

    birthday = Column(Date, default=date(2012, 1, 1), comment='生日')

    education = check_or_enum(name='education', enumList=['1', '2', '3'], comment='学历: 1->学士, 2->硕士, 3->博士')

    title = check_or_enum(name='title', enumList=['1', '2', '3', '4'], comment='职称: 1->助教, 2->讲师, 3->副教授, 4->教授')

    hashed_password = Column(String(60), server_default=get_password_hash('123456'), comment='密码')

    address = Column(String(20), server_default='广东省广州市', comment='上次登录地点')

    image = Column(String(60), server_default=f'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg', comment='头像')

    departmentId = Column(Integer, ForeignKey('department.id', ondelete='CASCADE'), nullable=False, doc='院系编号')

    taught = relationship('Taught')  # 不是字段, 可以通过 teacher ORM对象引用 taught 表的类集合
