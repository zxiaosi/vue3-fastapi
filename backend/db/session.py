#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:27
# @Author : zxiaosi
# @desc : 创建数据库会话
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# 数据库引擎
engine = create_engine(
    # 数据库uri
    settings.DATABASE_URI,

    # sqlite默认是单线程,开启多线程
    # connect_args={"check_same_thread": False},

    # 打印日志
    echo=settings.DATABASE_ECHO
)

# 创建本地会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 方便外部导入变量
__all__ = ["engine", "SessionLocal"]
