#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 管理员表
from sqlalchemy import Column, Integer, String, CheckConstraint, text

from db.base_class import Base


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

    sex = Column(String(5),
                 CheckConstraint("sex in ('man', 'woman')"),
                 default='man',
                 server_default=text("'man'"),
                 doc='管理员性别')

    password = Column(String(20), nullable=False, doc='管理员密码')
