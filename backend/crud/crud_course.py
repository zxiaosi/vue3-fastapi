#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 16:29
# @Author : zxiaosi
# @desc : 操作课程表
from crud.base import CRUDBase
from models import Course
from schemas import CourseCreate, CourseUpdate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):
    pass


course = CRUDCourse(Course)
