#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : zxiaosi
# @desc : 数据模型(类似于TS中的interface)
from .common import GMT
from .department import DepartmentCreate, DepartmentUpdate, DepartmentOut as Department
from .major import MajorCreate, MajorUpdate, MajorOut as Major
from .teacher import TeacherCreate, TeacherUpdate, TeacherOut as Teacher
from .student import StudentCreate, StudentUpdate, StudentOut as Student
from .course import CourseCreate, CourseUpdate, CourseOut as Course
from .selectCourse import SelectCourseCreate, SelectCourseUpdate, SelectCourseOut as SelectCourse
from .admin import AdminCreate, AdminUpdate, AdminOut as Admin
from .token import Token, TokenData
from .result import SchemasType, Result, ResultPlus
from .todo import TodoId, Todo
from .login import Login
