#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 22:08
# @Author : zxiaosi
# @desc : 创建与删除所有表
from db import engine
from models.base import Base
from utils import logger


def init_db():
    """ 创建 db/base 下的所有表 """
    try:
        drop_db()  # 删除所有的表
        Base.metadata.create_all(bind=engine)
        logger.info("创建表成功!!!")
    except Exception as e:
        logger.error(f"创建表失败!!! -- 错误信息如下:\n{e}")


def drop_db():
    """ 删除 db/base 下的所有表 """
    try:
        Base.metadata.drop_all(bind=engine)
        logger.info("删除表成功!!!")
    except Exception as e:
        logger.error(f"删除表失败!!! -- 错误信息如下:\n{e}")
