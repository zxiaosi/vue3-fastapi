#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/23 19:38
# @Author : 小四先生
# @desc : 初始化表数据尝试
import logging

from app02.db.session import SessionLocal
from app02.models.user import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()

    # User表
    new_User = User(user_id='2', full_name='李四', password='123')
    # 添加到db
    db.add(new_User)
    # 提交即保存到数据库
    db.commit()
    # 关闭db
    db.close()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")

