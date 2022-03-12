#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:50
# @Author : zxiaosi
# @desc : 两种初始化表数据的方式(添加的数据均没有验证类型)
from db import DBSession
from db.data import *
from models import *
from utils import logger
from utils.permission_assign import generate_permission_data


def db_conn(func):
    """ 连接数据库的装饰器 """

    def run():
        db = DBSession()  # 创建连接会话
        try:
            func(db)  # 运行sql语句
            db.commit()  # 提交事务
        except Exception as e:
            db.rollback()  # 如果出现错误，回滚事务
            logger.warning(f"运行时{str(func(db))}时出现错误，错误代码: \n{e}")  # 打印报错信息
        finally:
            db.close()  # 关闭数据库连接

    return run


@db_conn
def sqlalchemy_orm_initial(db):
    """ 初始化表数据方式一 : 速度欠佳 性能正常 """

    data = [
        *[Permission(**permission) for permission in generate_permission_data()],
        *[Department(**department) for department in departmentData],
        *[Major(**major) for major in majorData],
        *[Student(**student) for student in studentData],
        *[Teacher(**teacher) for teacher in teacherData],
        *[Course(**course) for course in courseData],
        *[SelectCourse(**selectCourse) for selectCourse in selectCourseData],
        *[Admin(**admin) for admin in adminData]
    ]

    # db.add_all(data)
    db.bulk_save_objects(data)
    logger.info("成功初始化所有表数据！！！")


@db_conn
def sqlalchemy_core_initial(db):
    """ 初始化表数据方式二 : 速度与性能并行 """

    # 插入数据
    db.execute(Permission.__table__.insert(), [permission for permission in generate_permission_data()]),
    db.execute(Department.__table__.insert(), [department for department in departmentData]),
    db.execute(Major.__table__.insert(), [major for major in majorData]),
    db.execute(Student.__table__.insert(), [student for student in studentData]),
    db.execute(Teacher.__table__.insert(), [teacher for teacher in teacherData]),
    db.execute(Admin.__table__.insert(), [admin for admin in adminData]),
    db.execute(Course.__table__.insert(), [course for course in courseData]),
    db.execute(SelectCourse.__table__.insert(), [selectCourse for selectCourse in selectCourseData])

    logger.info("成功初始化所有表数据！！！")
