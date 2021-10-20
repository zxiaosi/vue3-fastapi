#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 管理员表
from datetime import date

from sqlalchemy import Column, Integer, String, CheckConstraint, Date

from backend.db.base_class import Base


class Admin(Base):
    """ 管理员表 """
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                index=True,
                doc='职工号')

    name = Column(String(10),
                  nullable=False,
                  index=True,
                  doc='管理员姓名')

    sex = Column(String(2),
                 CheckConstraint("sex in ('男', '女')"),
                 nullable=False,
                 doc='管理员性别')

    birthday = Column(Date,
                      default=date(2012, 1, 1),
                      nullable=False,
                      doc='管理员生日')

    password = Column(String(20), nullable=False, doc='管理员密码')
