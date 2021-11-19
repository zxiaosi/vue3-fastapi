#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 16:42
# @Author : 小四先生
# @desc : 课程表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import CourseReturn, CourseCreate, CourseInDB, CourseUpdate
from utils import RestfulModel, response

router = APIRouter()


# 查询所有课程 or 根据 id 查询课程信息
@router.get("/",
            response_model=RestfulModel[Union[CourseReturn, List[CourseReturn]]],
            summary='查询所有课程 or 根据 id 查询课程信息')
def read_courses(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        courses_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """
        查询从 skip 到 limit 的课程 || 根据 id 查询课程信息
        - skip - 起始
        - limit - 末尾
        - courses_id - 课程编号
    """
    if courses_id:  # 根据 id 查询课程信息
        get_course = crud.course.get(db, id=courses_id)
        if not get_course:
            return response(code=404, msg=f"系统中不存在 id 为 {courses_id} 的课程.")
        return response(data=get_course, msg=f"查询到了 id 为 {courses_id} 的课程.")
    else:  # 查询从 skip 到 limit 的课程
        get_courses = crud.course.get_multi(db, skip=skip, limit=limit)
        return response(data=get_courses, msg=f"查询了从 {skip} 到 {limit} 之间的课程.")


# 添加课程信息
@router.post("/",
             response_model=RestfulModel[CourseInDB],
             summary='添加课程信息')
def create_course(
        *,
        db: Session = Depends(deps.get_db),
        course_in: CourseCreate,
) -> Any:
    """ 添加课程信息 """
    get_course = crud.course.get(db, id=course_in.id)
    if get_course:
        return response(code=400, msg=f"系统中已经存在 id 为 {course_in.id} 的课程.")
    add_course = crud.course.create(db, obj_in=course_in)
    return response(data=add_course, msg=f"添加了 id 为 {course_in.id} 的课程信息.")


# 通过 id 更新课程信息
@router.put("/{course_id}",
            response_model=RestfulModel[CourseInDB],
            summary='通过 id 更新课程信息')
def update_course(
        *,
        db: Session = Depends(deps.get_db),
        course_id: int,  # 防止用户输入字符串
        course_in: CourseUpdate,
) -> Any:
    """ 通过 id 更新课程信息 """
    get_course = crud.course.get(db, id=course_id)
    if not get_course:
        return response(code=404, msg=f"系统中不存在 id 为 {course_id} 的课程.")
    alter_course = crud.course.update(db, db_obj=get_course, obj_in=course_in)
    return response(data=alter_course, msg=f"更新了 id 为 {course_id} 的课程信息.")


# 通过 id 删除课程信息
@router.delete("/{course_id}",
               response_model=RestfulModel[CourseInDB],
               summary='通过 id 删除课程信息')
def delete_course(
        *,
        db: Session = Depends(deps.get_db),
        course_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除课程信息 """
    get_course = crud.course.get(db, id=course_id)
    if not get_course:
        return response(code=404, msg=f"系统中不存在 id 为 {course_id} 的课程.")
    del_course = crud.course.remove(db, id=course_id)
    return response(data=del_course, msg=f'成功删除 id 为 {course_id} 的课程信息')
