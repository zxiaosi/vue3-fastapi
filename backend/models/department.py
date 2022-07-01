#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : zxiaosi
# @desc : 院系表
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class Department(Base):
    """ 院系表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    name = Column(String(20), unique=True, nullable=False, index=True, comment='名字')

    chairman = Column(String(10), nullable=False, comment='主任姓名')

    phone = Column(String(11), comment='主任手机号')

    majors = relationship('Major')  # 不是字段, 可以通过 department ORM对象引用 major 表的类集合

    teachers = relationship('Teacher')  # 不是字段, 可以通过 department ORM对象引用 teacher 表的类集合
