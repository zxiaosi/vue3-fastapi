#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 9:48
# @Author : 小四先生
# @desc :
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import Teacher, TeacherInDB, TeacherCreate, TeacherUpdate
from utils import RestfulModel, response

router = APIRouter()


# 查询所有教师 or 通过 id 查询教师信息
@router.get("/",
            response_model=RestfulModel[Union[Teacher, List[Teacher]]],
            summary='查询所有教师 or 通过 id 查询教师信息')
def read_teachers(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        teacher_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """
        查询从 skip 到 limit 的教师 || 通过 id 查询教师信息
        - skip - 起始
        - limit - 末尾
        - teacher_id - 教师编号
    """
    if teacher_id:
        get_teacher = crud.teacher.get(db, id=teacher_id)
        if not get_teacher:
            return response(code=404, msg=f"系统中不存在 id 为 {teacher_id} 的教师.")
        return response(data=get_teacher, msg=f"查询到了 id 为 {teacher_id} 的教师.")
    else:
        get_teachers = crud.teacher.get_multi_teacher(db, skip=skip, limit=limit)
        return response(data=get_teachers, msg=f"查询了从 {skip} 到 {limit} 之间的教师.")


# 添加教师信息
@router.post("/",
             response_model=RestfulModel[TeacherInDB],
             summary='添加教师信息')
def create_teacher(
        *,
        db: Session = Depends(deps.get_db),
        teacher_in: TeacherCreate,
) -> Any:
    """ 添加教师信息 """
    get_teacher = crud.teacher.get(db, id=teacher_in.id)
    if get_teacher:
        return response(code=400, msg=f"系统中已经存在 id 为 {teacher_in.id} 的教师.")
    else:
        if crud.department.get(db=db, id=teacher_in.department_id):
            add_teacher = crud.teacher.create(db, obj_in=teacher_in)
            return response(msg=f"添加了 id 为 {teacher_in.id} 的教师信息.", data=add_teacher)
        else:
            return response(code=404, msg=f"系统中不存在 id 为 {teacher_in.department_id} 的院系.")


# 通过 id 更新教师信息
@router.put("/{teacher_id}",
            response_model=RestfulModel[TeacherInDB],
            summary='通过 id 更新教师信息')
def update_teacher(
        *,
        db: Session = Depends(deps.get_db),
        teacher_id: int,  # 防止用户输入字符串
        teacher_in: TeacherUpdate,
) -> Any:
    """ 通过 id 更新教师信息 """
    get_teacher = crud.teacher.get(db, id=teacher_id)
    if not get_teacher:
        return response(code=404, msg=f"系统中不存在 id 为 {teacher_id} 的教师.")
    else:
        if crud.department.get(db=db, id=teacher_in.department_id):
            alter_teacher = crud.teacher.update(db, db_obj=get_teacher, obj_in=teacher_in)
            return response(msg=f"更新了 id 为 {teacher_id} 的教师信息.", data=alter_teacher)
        else:
            return response(code=404, msg=f"系统中不存在 id 为 {teacher_in.department_id} 的院系.")


# 通过 id 删除教师信息
@router.delete("/{teacher_id}",
               response_model=RestfulModel[TeacherInDB],
               summary='通过 id 删除教师信息')
def delete_teacher(
        *,
        db: Session = Depends(deps.get_db),
        teacher_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除教师信息 """
    get_teacher = crud.teacher.get(db, id=teacher_id)
    if not get_teacher:
        return response(code=404, msg=f"系统中不存在 id 为 {teacher_id} 的教师.")
    del_teacher = crud.teacher.remove(db, id=teacher_id)
    return response(msg=f"删除了 id 为 {teacher_id} 的教师信息.", data=del_teacher)
