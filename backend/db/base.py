#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 9:53
# @Author : 小四先生
# @desc : 需要创建的表
"""(# nopa) 不可省略"""
from backend.db.base_class import Base  # noqa
# 调试表
from backend.models.user import User  # noqa
# 院系表
from backend.models.department import Department  # noqa
# 专业表
from backend.models.major import Major  # noqa
# 学生表
from backend.models.student import Student  # noqa
# 教师表
from backend.models.teacher import Teacher  # noqa
# 管理员表
from backend.models.admin import Admin  # noqa
# 课程表
from backend.models.course import Course  # noqa
# 选课表
from backend.models.selectCourse import SelectCourse  # noqa
# 控制表
from backend.models.control import Control  # noqa
