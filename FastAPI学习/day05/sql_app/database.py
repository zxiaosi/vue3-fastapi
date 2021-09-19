#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 14:08
# @Author : 小四先生
# @desc :
# 数据库地址
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# sqlite默认单线程，开启多线程
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 生成工厂类，然后再有工厂类生成session会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据表的结构 用 ORM 的语言描述出来
Base = declarative_base()
