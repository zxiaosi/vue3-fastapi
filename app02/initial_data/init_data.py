#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:50
# @Author : 小四先生
# @desc : 两种初始化表数据的方式
from app02.db import base
from app02.db.init_db import logger
from app02.db.session import Session
from app02.initial_data.data_orm import data
from app02.initial_data.data_core import userData, departmentData, majorData, studentData, teacherData, adminData, \
    courseData, selectCourseData
from app02.models.admin import Admin
from app02.models.course import Course
from app02.models.department import Department
from app02.models.major import Major
from app02.models.selectCourse import SelectCourse
from app02.models.student import Student
from app02.models.teacher import Teacher
from app02.models.user import User


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
            logger.warning(f"运行时{str(func(db))}时出现错误，错误代码: \n{e}")
        finally:
            # 关闭数据库连接
            db.close()

    return run


# 清空 base 下表的数据(待优化)
@db_conn
def clear_db(db):
    # 将表倒叙排列
    for table in reversed(base.Base.metadata.tables):
        db.execute(
            f"TRUNCATE TABLE {table};"
            f"SET FOREIGN_KEY_CHECKS = 0;"
        )
        # print(f"{table} 表数据已清空！！！")
    logger.info("所有表数据已清空！！！")


# 速度欠佳 性能正常
@db_conn
def sqlalchemy_orm_initial(db):
    # 清空表数据
    clear_db()

    # 将 data 添加到 db
    # db.add_all(data)
    db.bulk_save_objects(data)
    logger.info("成功初始化所有表数据！！！")


# 速度与性能并行
@db_conn
def sqlalchemy_core_initial(db):
    # 清空表数据
    clear_db()

    # 插入数据
    db.execute(
        # Table_name为表名
        User.__table__.insert(),
        # 列表生成式，包含大量的字典
        [user for user in userData]
    ),
    db.execute(Department.__table__.insert(), [department for department in departmentData]),
    db.execute(Major.__table__.insert(), [major for major in majorData]),
    db.execute(Student.__table__.insert(), [student for student in studentData]),
    db.execute(Teacher.__table__.insert(), [teacher for teacher in teacherData]),
    db.execute(Admin.__table__.insert(), [admin for admin in adminData]),
    db.execute(Course.__table__.insert(), [course for course in courseData]),
    db.execute(SelectCourse.__table__.insert(), [selectCourse for selectCourse in selectCourseData])

    logger.info("成功初始化所有表数据！！！")

# if __name__ == '__main__':
#     # sqlalchemy_orm_initial()
#     sqlalchemy_core_initial()
#     # clear_db()
