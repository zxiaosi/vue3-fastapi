#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:23
# @Author : 小四先生
# @desc : 院系表
from sqlalchemy import Column, String

from backend.db.base_class import Base


class Department(Base):
    department_id = Column(String(4),
                           primary_key=True,
                           index=True,
                           doc='院系编号')

    department_name = Column(String(20),
                             nullable=False,
                             index=True,
                             doc='院系名字')

    department_chairman = Column(String(10), nullable=False, doc='院系主任')

    department_phone = Column(String(11), nullable=False, doc='主任手机号')
