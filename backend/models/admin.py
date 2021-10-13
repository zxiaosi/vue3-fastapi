#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 管理员表
from sqlalchemy import Column, Integer, String, CheckConstraint, Date

from backend.db.base_class import Base


class Admin(Base):
    admin_id = Column(Integer,
                      primary_key=True,
                      autoincrement=True,
                      index=True,
                      doc='职工号')

    admin_name = Column(String(10),
                        nullable=False,
                        index=True,
                        doc='管理员姓名')

    admin_sex = Column(String(2),
                       CheckConstraint("admin_sex in ('男', '女')"),
                       nullable=False,
                       doc='管理员性别')

    admin_birthday = Column(Date,
                            server_default='2012-01-01',
                            nullable=False,
                            doc='管理员生日')

    admin_password = Column(String(20), nullable=False, doc='管理员密码')
