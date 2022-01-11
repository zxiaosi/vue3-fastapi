#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:01
# @Author : zxiaosi
# @desc : 操作院系表
from crud import CRUDBase
from models import Department
from schemas import DepartmentCreate, DepartmentUpdate


class CRUDDepartment(CRUDBase[Department, DepartmentCreate, DepartmentUpdate]):
    pass


department = CRUDDepartment(Department)
