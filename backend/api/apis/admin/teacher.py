#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 9:48
# @Author : zxiaosi
# @desc : 教师表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import TeacherOut, TeacherCreate, TeacherUpdate, ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有教师(根据页码和每页个数)
@router.get("/", response_model=ResultPlusModel[List[TeacherOut]], summary='查询所有教师(根据页码和每页个数)')
def read_teachers(db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
        查询所有教师(根据页码和每页个数)

        - pageIndex - 页码 (默认值 1)
        - pageSize - 每页个数 (默认值 10)
    """
    get_teachers = crud.teacher.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_teachers, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个教师信息.")


# 根据 id 查询教师信息
@router.get("/{id}", response_model=ResultModel[TeacherOut], summary='根据 id 查询教师信息')
def read_teacher(db: Session = Depends(deps.get_db), id: int = None) -> Any:
    """
        根据 id 查询教师信息

        - id - 职工号
    """
    get_teacher = crud.teacher.get(db, id=id)
    if not get_teacher:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    return resp_200(data=get_teacher, msg=f"查询到了 id 为 {id} 的教师.")


# 添加教师信息
@router.post("/", response_model=ResultModel[TeacherOut], summary='添加教师信息')
def create_teacher(*, db: Session = Depends(deps.get_db), teacher_in: TeacherCreate) -> Any:
    """ 添加教师信息(已添加异常捕获) """
    add_teacher = crud.teacher.create(db, obj_in=teacher_in)
    return resp_200(data=add_teacher, msg=f"添加了 id 为 {teacher_in.id} 的教师信息.")


# 通过 id 更新教师信息
@router.put("/{id}", response_model=ResultModel[TeacherOut], summary='通过 id 更新教师信息')
def update_teacher(*, db: Session = Depends(deps.get_db), id: int, teacher_in: TeacherUpdate) -> Any:
    """ 通过 id 更新教师信息(已添加异常捕获) """
    get_teacher = crud.teacher.get(db, id=id)
    if not get_teacher:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    else:
        alter_teacher = crud.teacher.update(db, db_obj=get_teacher, obj_in=teacher_in)
        return resp_200(data=alter_teacher, msg=f"更新了 id 为 {id} 的教师信息.")


# 通过 id 删除教师信息
@router.delete("/{id}", response_model=ResultModel[TeacherOut], summary='通过 id 删除教师信息')
def delete_teacher(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """ 通过 id 删除教师信息 """
    del_teacher = crud.teacher.remove(db, id=id)
    return resp_200(data=del_teacher, msg=f"删除了 id 为 {id} 的教师信息.")