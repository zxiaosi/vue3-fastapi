#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 22:08
# @Author : 小四先生
# @desc : 初始化表
from app02.db import base
from app02.db.session import engine


# 创建 base 下的所有表
def init_db():
    base.Base.metadata.create_all(bind=engine)


# 删除 base 下的所有表
def drop_db():
    base.Base.metadata.drop_all(bind=engine)


if __name__ == '__main__':
    init_db()
    # drop_db()
