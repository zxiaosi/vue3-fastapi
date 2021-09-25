#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:13
# @Author : 小四先生
# @desc : user表(调试)
from sqlalchemy import Column, Integer, String, Boolean, DateTime, text, CheckConstraint

from app02.db.base_class import Base


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

    user_id = Column(Integer,
                     primary_key=True,
                     autoincrement=True,
                     index=True,
                     doc='主键')

    full_name = Column(String(10),
                       unique=True,
                       nullable=False,
                       doc='全名')

    # sex = Column(String(2),
    #              CheckConstraint("sex in ('男', '女')"),
    #              nullable=False)
    #
    # birthday = Column(DateTime,
    #                   nullable=False,
    #                   server_default=text('CURRENT_TIMESTAMP')
    #                   )
    password = Column(String(20), nullable=False)

    # is_active = Column(Boolean(), default=True)
    # is_superuser = Column(Boolean(), default=False)
