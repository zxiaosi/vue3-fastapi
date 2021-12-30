#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : 小四先生
# @desc : Pydantic数据验证
""" 抛出Pydantic数据验证 """
from .user import UserCreate, UserUpdate, User, UserInDB
from .department import DepartmentCreate, DepartmentUpdate, DepartmentReturn, DepartmentInDB
from .major import MajorCreate, MajorUpdate, MajorReturn, MajorInDB
from .teacher import TeacherCreate, TeacherUpdate, TeacherReturn, TeacherInDB
from .student import StudentCreate, StudentUpdate, StudentReturn, StudentInDB
from .course import CourseCreate, CourseUpdate, CourseReturn, CourseInDB
from .selectCourse import SelectCourseCreate, SelectCourseUpdate, SelectCourseReturn, SelectCourseInDB
from .token import Token, TokenPayload
