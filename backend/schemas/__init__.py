#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : zxiaosi
# @desc : 加载Pydantic数据验证
from .user import UserCreate, UserUpdate, User, UserInDB
from .department import DepartmentCreate, DepartmentUpdate, DepartmentOut
from .major import MajorCreate, MajorUpdate, MajorOut
from .teacher import TeacherCreate, TeacherUpdate, TeacherOut
from .student import StudentCreate, StudentUpdate, StudentOut
from .course import CourseCreate, CourseUpdate, CourseOut
from .selectCourse import SelectCourseCreate, SelectCourseUpdate, SelectCourseOut
from .admin import Admin, AdminInDB
from .token import Token, TokenPayload
from .result import ResultModel, ResultPlusModel
