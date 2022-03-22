#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:40
# @Author : zxiaosi
# @desc : 数据模型(类似于TS中的interface)
from .common import GMT, Relation
from .department import DepartmentCreate, DepartmentUpdate, DepartmentOut
from .major import MajorCreate, MajorUpdate, MajorOut
from .teacher import TeacherCreate, TeacherUpdate, TeacherOut
from .student import StudentCreate, StudentUpdate, StudentOut
from .course import CourseCreate, CourseUpdate, CourseOut
from .selectCourse import SelectCourseCreate, SelectCourseUpdate, SelectCourseOut
from .admin import AdminCreate, AdminUpdate, AdminOut
from .token import Token, TokenData
from .result import SchemasType, ResultModel, ResultPlusModel
from .todo import TodoId, Todo
from .login import Login
