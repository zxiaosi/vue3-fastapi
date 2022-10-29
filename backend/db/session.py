#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:27
# @Author : zxiaosi
# @desc : 数据库会话
# https://www.osgeo.cn/sqlalchemy/orm/extensions/asyncio.html?highlight=async#asynchronous-i-o-asyncio
from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

from core import settings

# 创建表引擎
engine = create_async_engine(
    url=settings.DATABASE_URI,  # 数据库uri
    echo=settings.DATABASE_ECHO,  # 是否打印日志
    # pool_size=10,  # 队列池个数
    # max_overflow=20,  # 队列池最大溢出个数
    pool_pre_ping=True
)

# 操作表会话
async_session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # 防止提交后属性过期
)

async_session = async_scoped_session(async_session_factory, scopefunc=current_task)
