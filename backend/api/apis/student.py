#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:12
# @Author : 小四先生
# @desc : 学生表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import StudentReturn, StudentInDB, StudentCreate, StudentUpdate
from utils import RestfulModel, response

router = APIRouter()


# 查询所有学生 or 通过 id 查询学生信息
@router.get("/",
            response_model=RestfulModel[Union[StudentReturn, List[StudentReturn]]],
            summary='查询所有学生 or 通过 id 查询学生信息')
def read_students(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        student_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """
        查询从 skip 到 limit 的学生 || 通过 id 查询学生信息
        - skip - 起始
        - limit - 末尾
        - student_id - 学生编号
    """
    if student_id:
        get_student = crud.student.get_multi_student(db, id=student_id)
        if not get_student:
            return response(code=404, msg=f"系统中不存在 id 为 {student_id} 的学生.")
        return response(data=get_student, msg=f"查询到了 id 为 {student_id} 的学生.")
    else:
        get_students = crud.student.get_multi_student(db, skip=skip, limit=limit)
        return response(data=get_students, msg=f"查询了从 {skip} 到 {limit} 之间的学生.")


# 添加学生信息
@router.post("/",
             response_model=RestfulModel[StudentInDB],
             summary='添加学生信息')
def create_student(
        *,
        db: Session = Depends(deps.get_db),
        student_in: StudentCreate,
) -> Any:
    """ 添加学生信息 """
    get_student = crud.student.get(db, id=student_in.id)
    if get_student:
        return response(code=400, msg=f"系统中已经存在 id 为 {student_in.id} 的学生.")
    else:
        if crud.major.get(db=db, id=student_in.major_id):
            add_student = crud.student.create(db, obj_in=student_in)
            return response(msg=f"添加了 id 为 {student_in.id} 的学生信息.", data=add_student)
        else:
            return response(code=404, msg=f"系统中不存在 id 为 {student_in.major_id} 的专业.")


# 通过 id 更新学生信息
@router.put("/{student_id}",
            response_model=RestfulModel[StudentInDB],
            summary='通过 id 更新学生信息')
def update_student(
        *,
        db: Session = Depends(deps.get_db),
        student_id: int,  # 防止用户输入字符串
        student_in: StudentUpdate,
) -> Any:
    """ 通过 id 更新学生信息 """
    get_student = crud.student.get(db, id=student_id)
    if not get_student:
        return response(code=404, msg=f"系统中不存在 id 为 {student_id} 的学生.")
    else:
        if crud.major.get(db=db, id=student_in.major_id):
            alter_student = crud.student.update(db, db_obj=get_student, obj_in=student_in)
            return response(msg=f"更新了 id 为 {student_id} 的学生信息.", data=alter_student)
        else:
            return response(code=404, msg=f"系统中不存在 id 为 {student_in.major_id} 的专业.")


# 通过 id 删除学生信息
@router.delete("/{student_id}",
               response_model=RestfulModel[StudentInDB],
               summary='通过 id 删除学生信息')
def delete_student(
        *,
        db: Session = Depends(deps.get_db),
        student_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除学生信息 """
    get_student = crud.student.get(db, id=student_id)
    if not get_student:
        return response(code=404, msg=f"系统中不存在 id 为 {student_id} 的学生.")
    del_student = crud.student.remove(db, id=student_id)
    return response(msg=f"删除了 id 为 {student_id} 的学生信息.", data=del_student)
