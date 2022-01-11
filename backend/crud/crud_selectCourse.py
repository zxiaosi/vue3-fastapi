#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:09
# @Author : zxiaosi
# @desc : 操作选课表
from crud.base import CRUDBase
from models import SelectCourse
from schemas import SelectCourseCreate, SelectCourseUpdate


class CRUDSelectCourse(CRUDBase[SelectCourse, SelectCourseCreate, SelectCourseUpdate]):
    pass


selectCourse = CRUDSelectCourse(SelectCourse)
