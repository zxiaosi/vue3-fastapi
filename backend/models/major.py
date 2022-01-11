#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : zxiaosi
# @desc : 专业表
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base_class import Base


class Major(Base):
    """ 专业表 """
    id = Column(String(6), primary_key=True, index=True, doc='专业编号')

    name = Column(String(20), unique=True, nullable=False, doc='专业名字')

    assistant = Column(String(10), nullable=False, doc='辅导员姓名')

    phone = Column(String(11), doc='辅导员手机号')

    department_id = Column(String(4), ForeignKey('department.id'), doc='院系编号')

    department = relationship("Department", backref=backref("major", cascade="all, delete"))
