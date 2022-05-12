#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : zxiaosi
# @desc : 专业表
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Major(Base):
    """ 专业表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    name = Column(String(20), unique=True, nullable=False, comment='名字')

    assistant = Column(String(10), nullable=False, comment='辅导员姓名')

    phone = Column(String(11), comment='辅导员手机号')

    departmentId = Column(Integer, ForeignKey('department.id', ondelete='CASCADE'), nullable=False, comment='院系编号')

    students = relationship('Student')  # 不是字段, 可以通过 major ORM对象引用 student 表的类集合
