#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 教师表
from datetime import date
from sqlalchemy import Column, String, ForeignKey, CheckConstraint, Date, Boolean, text, TIMESTAMP, func

from core import settings
from models import Base


class Teacher(Base):
    """ 教师表 """
    id = Column(String(6), primary_key=True, index=True, comment='职工号')

    name = Column(String(10), unique=True, nullable=False, comment='姓名')

    sex = Column(String(1), CheckConstraint("sex in ('0', '1')"), server_default=text("'0'"),
                 comment='性别: 0 -> 男, 1 -> 女')

    birthday = Column(Date, default=date(2012, 1, 1), nullable=False, comment='生日')

    education = Column(String(1), CheckConstraint("education in ('1', '2', '3')"), server_default=text("'1'"),
                       comment='学历: 1 -> 学士, 2 -> 硕士, 3 -> 博士')

    title = Column(String(1), CheckConstraint("title in ('1', '2', '3', '4')"), server_default=text("'1'"),
                   comment='职称: 1 -> 助教, 2 -> 讲师, 3 -> 副教授, 4 -> 教授')

    address = Column(String(20), server_default=text("'广东省广州市'"), comment='地址')

    image = Column(String(60), server_default=text(f"'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg'"),
                   comment='头像')

    hashed_password = Column(String(60), nullable=False, comment='密码')

    is_active = Column(Boolean(), server_default=text("True"), comment='是否登录')

    department_id = Column(String(4), ForeignKey('department.id', ondelete='CASCADE'), doc='院系编号')

    gmt_create = Column(TIMESTAMP(True), server_default=func.now(), comment='创建时间')

    gmt_modify = Column(TIMESTAMP(True), server_default=func.now(), onupdate=func.now(), comment='更新时间')
