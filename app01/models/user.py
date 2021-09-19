#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 17:13
# @Author : 小四先生
# @desc : user表
import enum

from sqlalchemy import Column, Integer, String, Boolean, DateTime, text, CheckConstraint

from app01.db.base_class import Base


class SexEnum(enum.Enum):
    male = '男'
    female = '女'


class User(Base):
    # primary_key 主键
    # index 索引
    # autoincrement 自增
    # nullable=False 不为空
    # server_default 默认值
    # unique 唯一
    # comment 注释
    # doc 记录属性
    # CheckConstraint check约束

    # CURRENT_TIMESTAMP 当前时间
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(10), index=True, doc='全名', nullable=False, unique=True)
    email = Column(String(18), index=True)
    sex = Column(String(2), CheckConstraint("sex in ('男', '女')"), nullable=False)
    birthday = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    hashed_password = Column(String(20), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

