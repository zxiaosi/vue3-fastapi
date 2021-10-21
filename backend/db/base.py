#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 9:53
# @Author : 小四先生
# @desc : 需要创建的表
"""(# nopa) 不可省略"""
from db.base_class import Base  # noqa
# 调试表
from models.user import User  # noqa
# 院系表
from models.department import Department  # noqa
# 专业表
from models.major import Major  # noqa
# 学生表
from models.student import Student  # noqa
# 教师表
from models.teacher import Teacher  # noqa
# 管理员表
from models.admin import Admin  # noqa
# 课程表
from models.course import Course  # noqa
# 选课表
from models.selectCourse import SelectCourse  # noqa
# 控制表
from models.control import Control  # noqa
