#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 课程表
from sqlalchemy import Column, String, Float, SmallInteger, Integer
from sqlalchemy.orm import relationship

from models import Base


class Course(Base):
    """ 课程表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    name = Column(String(20), unique=True, nullable=False, comment='名字')

    credit = Column(Float, default=0, server_default='0', comment='学分')

    period = Column(SmallInteger, server_default='0', comment='课时')

    taught = relationship('Taught')  # 不是字段, 可以通过 course ORM对象引用 taught 表的类集合

    elective = relationship('Elective')  # 不是字段, 可以通过 elective ORM对象引用 taught 表的类集合
