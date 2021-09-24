#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 9:53
# @Author : 小四先生
# @desc : 声明需要 创建的表
from app02.db.base_class import Base  # noqa
# 院系表
from app02.models.department import Department  # noqa
# 专业表
from app02.models.major import Major  # noqa
# 学生表
from app02.models.student import Student  # noqa
# 教师表
from app02.models.teacher import Teacher  # noqa
# 管理员表
from app02.models.admin import Admin  # noqa
# 课程表
from app02.models.course import Course  # noqa
# 选课表
from app02.models.selectCourse import SelectCourse  # noqa
# 控制表
from app02.models.control import Control  # noqa
# 调试表
from app02.models.user import User  # noqa

