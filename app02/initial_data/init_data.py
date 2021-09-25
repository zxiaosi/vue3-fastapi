#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:50
# @Author : 小四先生
# @desc : 两种初始化表数据的方式
from app02.db.session import Session
from app02.initial_data.data_orm import data
from app02.initial_data.data_core import userData

from app02.models.user import User


# 速度略慢,性能正常
def db_conn(func):
    def run():
        # 创建连接会话
        db = Session()
        try:
            # 运行sql语句
            func(db)
            # 提交事务
            db.commit()
        except Exception as e:
            # 如果出现错误，回滚事务
            db.rollback()
            # 打印报错信息
            print(f'运行时{str(func(db))}时出现错误，错误代码: {e}')
        finally:
            # 关闭数据库连接
            db.close()

    return run


# 速度欠佳 性能正常
@db_conn
def sqlalchemy_orm_initial(db):
    print(f'我执行了--{db}')
    # db.add_all(data)
    db.bulk_save_objects(data)


# 速度与性能并行
@db_conn
def sqlalchemy_core_initial(db):
    # 将 data 添加到db
    db.execute(
        # Table_name为表名
        User.__table__.insert(),
        # 列表生成式，包含大量的字典
        [{'user_id': user['id'], 'full_name': user['name'], 'password': user['pwd']} for user in userData],
    )


if __name__ == '__main__':
    # sqlalchemy_orm_initial()
    sqlalchemy_core_initial()
