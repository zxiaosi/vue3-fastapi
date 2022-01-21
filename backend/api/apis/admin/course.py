#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 16:42
# @Author : zxiaosi
# @desc : 课程表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import CourseCreate, CourseUpdate, CourseOut, ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有课程(根据页码和每页个数)
@router.get("/", response_model=ResultPlusModel[List[CourseOut]], summary='查询所有课程(根据页码和每页个数)')
def read_courses(db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
        查询所有课程(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

        - pageIndex - 页码 (默认值 1)
        - pageSize - 每页个数 (默认值 10)
    """
    get_courses = crud.course.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    if pageIndex == -1 and pageSize == -1:
        text = "查询了所有的课程信息."
    else:
        text = f"查询了第 {pageIndex} 页中的 {pageSize} 个课程信息."
    return resp_200(data=get_courses, msg=text)


# 根据 id 查询课程信息
@router.get("/{id}", response_model=ResultModel[CourseOut], summary='根据 id 查询课程信息')
def read_course(db: Session = Depends(deps.get_db), id: int = None) -> Any:
    """
        根据 id 查询课程信息

        - id - 课程编号
    """
    get_course = crud.course.get(db, id=id)
    if not get_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    return resp_200(data=get_course, msg=f"查询到了 id 为 {id} 的课程.")


# 添加课程信息
@router.post("/", response_model=ResultModel[CourseOut], summary='添加课程信息')
def create_course(*, db: Session = Depends(deps.get_db), course_in: CourseCreate) -> Any:
    """ 添加课程信息(已添加异常捕获) """
    add_course = crud.course.create(db, obj_in=course_in)
    return resp_200(data=add_course, msg=f"添加了 id 为 {course_in.id} 的课程信息.")


# 通过 id 更新课程信息
@router.put("/{id}", response_model=ResultModel[CourseOut], summary='通过 id 更新课程信息')
def update_course(*, db: Session = Depends(deps.get_db), id: int, course_in: CourseUpdate) -> Any:
    """ 通过 id 更新课程信息(已添加异常捕获) """
    get_course = crud.course.get(db, id=id)
    if not get_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    alter_course = crud.course.update(db, db_obj=get_course, obj_in=course_in)
    return resp_200(data=alter_course, msg=f"更新了 id 为 {id} 的课程信息.")


# 通过 id 删除课程信息
@router.delete("/{id}", response_model=ResultModel[CourseOut], summary='通过 id 删除课程信息')
def delete_course(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """ 通过 id 删除课程信息(已添加异常捕获) """
    del_course = crud.course.remove(db, id=id)
    return resp_200(data=del_course, msg=f'成功删除 id 为 {id} 的课程信息')


# 只获取关系字段
@router.get("/relation/", response_class=ORJSONResponse, summary='获取到 课程表 中的关系字段')
def get_student_relation(db: Session = Depends(deps.get_db)) -> Any:
    """ 只获取关系字段 """
    get_students = crud.course.get_multi_relation(db)
    return resp_200(data=get_students, msg="获取到 课程表 中的关系字段.")
