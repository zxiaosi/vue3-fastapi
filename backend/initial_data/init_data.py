#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:50
# @Author : zxiaosi
# @desc : 两种初始化表数据的方式(添加的数据均没有验证类型)
from utils import logger
from db import base, init_db, SessionLocal
from initial_data.data import *
from models import *


# 连接数据库的装饰器
def db_conn(func):
    """ 连接数据库的装饰器 """

    def run():
        db = SessionLocal()  # 创建连接会话
        try:
            func(db)  # 运行sql语句
            db.commit()  # 提交事务
        except Exception as e:
            db.rollback()  # 如果出现错误，回滚事务
            logger.warning(f"运行时{str(func(db))}时出现错误，错误代码: \n{e}")  # 打印报错信息
        finally:
            db.close()  # 关闭数据库连接

    return run


# 清空 db/base 下表的数据(MySQL使用, SQLite中报错)
@db_conn
def clear_db(db):
    """ 清空 db/base 下表的数据(MySQL使用) """
    # 将表倒叙排列
    for table in reversed(base.Base.metadata.tables):
        db.execute(
            f"TRUNCATE TABLE {table};"
            f"SET FOREIGN_KEY_CHECKS = 0;"
        )
    logger.info("所有表数据已清空！！！")


# 速度欠佳 性能正常
@db_conn
def sqlalchemy_orm_initial(db):
    """ 初始化表数据方式一 : 速度欠佳 性能正常 """
    # 清空表数据
    # clear_db()

    data = [
        *[User(**user) for user in userData], *[Department(**department) for department in departmentData],
        *[Major(**major) for major in majorData], *[Student(**student) for student in studentData],
        *[Teacher(**teacher) for teacher in teacherData], *[Course(**course) for course in courseData],
        *[SelectCourse(**selectCourse) for selectCourse in selectCourseData],
        *[Admin(**admin) for admin in adminData]
    ]

    # db.add_all(data)
    db.bulk_save_objects(data)
    logger.info("成功初始化所有表数据！！！")


# 速度与性能并行
@db_conn
def sqlalchemy_core_initial(db):
    """ 初始化表数据方式二 : 速度与性能并行 """
    # 清空表数据
    # clear_db()

    # 插入数据
    db.execute(
        User.__table__.insert(),  # Table_name为表名
        [user for user in userData]  # 列表生成式，包含大量的字典
    ),
    db.execute(Department.__table__.insert(), [department for department in departmentData]),
    db.execute(Major.__table__.insert(), [major for major in majorData]),
    db.execute(Student.__table__.insert(), [student for student in studentData]),
    db.execute(Teacher.__table__.insert(), [teacher for teacher in teacherData]),
    db.execute(Admin.__table__.insert(), [admin for admin in adminData]),
    db.execute(Course.__table__.insert(), [course for course in courseData]),
    db.execute(SelectCourse.__table__.insert(), [selectCourse for selectCourse in selectCourseData])

    logger.info("成功初始化所有表数据！！！")


if __name__ == '__main__':
    init_db()
    sqlalchemy_orm_initial()
    # sqlalchemy_core_initial()
    # clear_db()
