#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/23 19:38
# @Author : 小四先生
# @desc : 初始化表数据尝试
from backend.test.db_init.data import userData, data
from backend.db.session import SessionLocal
from backend.models.user import User


# 速度略慢,性能正确
def init_first():
    db = SessionLocal()
    # 将 userData 添加到db
    db.add_all(userData)
    db.bulk_save_objects(userData)
    # 提交即保存到数据库
    db.commit()
    # 关闭db
    db.close()


# 速度与性能并行
def init_second():
    db = SessionLocal()
    # 将 data 添加到db
    db.execute(
        # Table_name为表名
        User.__table__.insert(),
        # 列表生成式，包含大量的字典
        [{'user_id': user['user_id'], 'full_name': user['full_name'], 'password': user['password']} for user in data],
    )
    # 提交即保存到数据库
    db.commit()
    # 关闭db
    db.close()


if __name__ == '__main__':
    # init_first()
    init_second()
