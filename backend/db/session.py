#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:27
# @Author : zxiaosi
# @desc : 数据库会话
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import settings


def is_open_thread():
    """ 是否关闭sqlite单线程 """
    if settings.DATABASE_URI.startswith('sqlite'):
        return {"check_same_thread": False}
    else:
        return ''


# 数据库引擎
engine = create_engine(
    url=settings.DATABASE_URI,  # 数据库uri
    connect_args=is_open_thread(),  # sqlite默认是单线程,使用sqlite需关闭单线程
    echo=settings.DATABASE_ECHO  # 是否打印日志
)

# 创建本地会话
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
