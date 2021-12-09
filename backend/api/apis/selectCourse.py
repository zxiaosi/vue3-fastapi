#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:25
# @Author : 小四先生
# @desc : 选课表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import SelectCourseReturn, SelectCourseInDB, SelectCourseCreate, SelectCourseUpdate
from utils import RestfulModel, response

router = APIRouter()


# 查询所有选课 or 通过 id 查询选课信息
@router.get("/",
            response_model=RestfulModel[Union[SelectCourseReturn, List[SelectCourseReturn]]],
            summary='查询所有选课 or 通过 id 查询选课信息')
def read_select_courses(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        select_course_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """
        查询从 skip 到 limit 的选课 || 通过 id 查询选课信息
        - skip - 起始
        - limit - 末尾
        - select_course_id - 选课编号
    """
    if select_course_id:
        get_select_course = crud.selectCourse.get(db, id=select_course_id)
        if not get_select_course:
            return response(code=404, msg=f"系统中不存在 id 为 {select_course_id} 的选课.")
        return response(data=get_select_course, msg=f"查询到了 id 为 {select_course_id} 的选课.")
    else:
        get_select_courses = crud.selectCourse.get_multi(db, skip=skip, limit=limit)
        return response(data=get_select_courses, msg=f"查询了从 {skip} 到 {limit} 之间的选课.")


# 添加选课信息
@router.post("/",
             response_model=RestfulModel[SelectCourseInDB],
             summary='添加选课信息')
def create_select_course(
        *,
        db: Session = Depends(deps.get_db),
        select_course_in: SelectCourseCreate,
) -> Any:
    """ 添加选课信息 """
    if not crud.student.get(db=db, id=select_course_in.student_id):
        return response(code=404, msg=f"系统中不存在 id 为 {select_course_in.student_id} 的学生.")
    elif not crud.teacher.get(db=db, id=select_course_in.teacher_id):
        return response(code=404, msg=f"系统中不存在 id 为 {select_course_in.teacher_id} 的教师.")
    elif not crud.course.get(db=db, id=select_course_in.course_id):
        return response(code=404, msg=f"系统中不存在 id 为 {select_course_in.course_id} 的课程.")
    else:
        add_select_course = crud.selectCourse.create(db, obj_in=select_course_in)
        return response(msg=f"添加了选课信息.", data=add_select_course)


# 通过 id 更新选课信息
@router.put("/{select_course_id}",
            response_model=RestfulModel[SelectCourseInDB],
            summary='通过 id 更新选课信息')
def update_select_course(
        *,
        db: Session = Depends(deps.get_db),
        select_course_id: int,  # 防止用户输入字符串
        select_course_in: SelectCourseUpdate,
) -> Any:
    """ 通过 id 更新选课信息 """
    get_select_course = crud.selectCourse.get(db, id=select_course_id)
    if not get_select_course:
        return response(code=404, msg=f"系统中不存在 id 为 {select_course_id} 的选课.")
    else:
        if not crud.student.get(db=db, id=select_course_in.student_id):
            return response(code=404, msg=f"系统中不存在 id 为 {select_course_in.student_id} 的学生.")
        elif not crud.teacher.get(db=db, id=select_course_in.teacher_id):
            return response(code=404, msg=f"系统中不存在 id 为 {select_course_in.teacher_id} 的教师.")
        elif not crud.course.get(db=db, id=select_course_in.course_id):
            return response(code=404, msg=f"系统中不存在 id 为 {select_course_in.course_id} 的课程.")
        else:
            alter_select_course = crud.selectCourse.update(db, db_obj=get_select_course, obj_in=select_course_in)
            return response(msg=f"更新了 id 为 {select_course_id} 的选课信息.", data=alter_select_course)


# 通过 id 删除选课信息
@router.delete("/{select_course_id}",
               response_model=RestfulModel[SelectCourseInDB],
               summary='通过 id 删除选课信息')
def delete_select_course(
        *,
        db: Session = Depends(deps.get_db),
        select_course_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除选课信息 """
    get_select_course = crud.selectCourse.get(db, id=select_course_id)
    if not get_select_course:
        return response(code=404, msg=f"系统中不存在 id 为 {select_course_id} 的选课.")
    del_select_course = crud.selectCourse.remove(db, id=select_course_id)
    return response(msg=f"删除了 id 为 {select_course_id} 的选课信息.", data=del_select_course)
