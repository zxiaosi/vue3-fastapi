#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 22:08
# @Author : zxiaosi
# @desc : 创建与删除所有表, 初始化数据
from core.logger import logger
from db import engine
from db.data import *
from models import Base, Department, Major, Student, Teacher, Admin, Course, Taught, Elective


async def init_db():
    """ 创建 models/__init__ 下的所有表 """
    try:
        await drop_db()  # 删除所有的表
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("创建表成功!!!")
    except Exception as e:
        logger.error(f"创建表失败!!! -- 错误信息如下:\n{e}")
    finally:
        await engine.dispose()


async def drop_db():
    """ 删除 models/__init__ 下的所有表 """
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        logger.info("删除表成功!!!")
    except Exception as e:
        logger.error(f"删除表失败!!! -- 错误信息如下:\n{e}")
    finally:
        await engine.dispose()


async def init_data():
    """ 初始化表数据 """
    try:
        async with engine.begin() as conn:
            await conn.execute(Department.__table__.insert(), [department for department in departmentData])
            await conn.execute(Major.__table__.insert(), [major for major in majorData])
            await conn.execute(Student.__table__.insert(), [student for student in studentData])
            await conn.execute(Teacher.__table__.insert(), [teacher for teacher in teacherData])
            await conn.execute(Admin.__table__.insert(), [admin for admin in adminData])
            await conn.execute(Course.__table__.insert(), [course for course in courseData])
            await conn.execute(Taught.__table__.insert(), [selectCourse for selectCourse in taughtData])
            await conn.execute(Elective.__table__.insert(), [selectCourse for selectCourse in electiveData])
            logger.info(f"成功初始化表数据!!!")
    except Exception as e:
        logger.error(f"初始化表数据失败!!! -- 错误信息如下:\n{e}")
    finally:
        await engine.dispose()
