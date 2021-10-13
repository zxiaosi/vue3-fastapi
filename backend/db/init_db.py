#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 22:08
# @Author : 小四先生
# @desc : 创建与删除所有表
from backend.core.config import logger
from backend.db import base
from backend.db.session import engine


# 创建 base 下的所有表
def init_db():
    try:
        # 删除所有的表
        drop_db()

        base.Base.metadata.create_all(bind=engine)
        logger.info("创建表成功!!!")

    except Exception as e:
        logger.warning(f"创建表失败!!! -- 错误信息如下:\n{e}")


# 删除 base 下的所有表
def drop_db():
    try:
        base.Base.metadata.drop_all(bind=engine)
        logger.info("删除表成功!!!")
    except Exception as e:
        logger.warning(f"删除表失败!!! -- 错误信息如下:\n{e}")


if __name__ == '__main__':
    init_db()
    # drop_db()
