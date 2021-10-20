#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : 小四先生
# @desc : 专业表
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.db.base_class import Base

if TYPE_CHECKING:
    from .department import Department  # noqa


class Major(Base):
    """ 专业表 """
    id = Column(String(6),
                primary_key=True,
                index=True,
                doc='专业编号')

    name = Column(String(20),
                  nullable=False,
                  index=True,
                  doc='专业名字')

    assistant = Column(String(10), nullable=False, doc='辅导员')

    phone = Column(String(11), nullable=False, doc='辅导员手机号')

    department_id = Column(String(4), ForeignKey('department.id'), doc='院系编号')

    department = relationship("Department", backref="major")
