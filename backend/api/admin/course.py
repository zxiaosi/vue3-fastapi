#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 16:42
# @Author : zxiaosi
# @desc : 课程表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db, get_current_user
from models import Admin
from schemas import CourseCreate, CourseUpdate, CourseOut, Relation, ResultModel, ResultPlusModel
from crud import course
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/", response_model=ResultPlusModel[List[CourseOut]], summary='查询所有课程(根据页码和每页个数)')
def read_courses(
        db: Session = Depends(get_db),
        pageIndex: int = 1,
        pageSize: int = 10,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    """
    查询所有课程(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

    - pageIndex - 页码 (默认值 1)
    - pageSize - 每页个数 (默认值 10)
    """
    get_courses = course.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_courses, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个课程信息.")


@router.get("/{id}", response_model=ResultPlusModel[CourseOut], summary='根据 id 查询课程信息')
def read_course(*, db: Session = Depends(get_db), id: int, current_user: Admin = Depends(get_current_user)) -> Any:
    get_course = course.get(db, id=id)
    if not get_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    return resp_200(data=get_course, msg=f"查询到了 id 为 {id} 的课程.")


@router.post("/", response_model=ResultModel[CourseOut], summary='添加课程信息')
def create_course(
        *,
        db: Session = Depends(get_db),
        course_in: CourseCreate,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    add_course = course.create(db, obj_in=course_in)
    return resp_200(data=add_course, msg=f"添加了 id 为 {course_in.id} 的课程信息.")


@router.put("/{id}", response_model=ResultModel[CourseOut], summary='通过 id 更新课程信息')
def update_course(
        *,
        db: Session = Depends(get_db),
        id: int,
        course_in: CourseUpdate,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    get_course = course.get(db, id=id)
    if not get_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    alter_course = course.update(db, db_obj=get_course, obj_in=course_in)
    return resp_200(data=alter_course, msg=f"更新了 id 为 {id} 的课程信息.")


@router.delete("/{id}", response_model=ResultModel[CourseOut], summary='通过 id 删除课程信息')
def delete_course(*, db: Session = Depends(get_db), id: int, current_user: Admin = Depends(get_current_user)) -> Any:
    del_course = course.remove(db, id=id)
    return resp_200(data=del_course, msg=f'成功删除 id 为 {id} 的课程信息')


@router.post("/del/", response_model=ResultModel, summary='同时删除多个课程信息')
def delete_courses(
        *,
        db: Session = Depends(get_db),
        idList: list,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    course.remove_multi(db, id_list=idList)
    return resp_200(data='', msg=f'同时删除多个课程信息.')


@router.get("/relation/", response_model=ResultModel[Relation], summary='获取到 课程表 中的关系字段')
def get_course_relation(db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)) -> Any:
    get_courses = course.get_multi_relation(db)
    return resp_200(data=get_courses, msg="获取到 课程表 中的关系字段.")
