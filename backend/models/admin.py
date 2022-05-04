#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : zxiaosi
# @desc : 管理员表
from sqlalchemy import Column, Integer, String, text

from core import settings, get_password_hash
from models import Base


class Admin(Base):
    """ 管理员表 """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')

    name = Column(String(10), nullable=False, index=True, comment='姓名')

    address = Column(String(20), server_default='广东省广州市', comment='上次登录地址')

    image = Column(String(60), server_default=f'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg', comment='头像')

    hashed_password = Column(String(60), server_default=get_password_hash('123456'), comment='密码')
