#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:12
# @Author : zxiaosi
# @desc : 学生表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import StudentCreate, StudentUpdate, StudentOut, ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有学生(根据页码和每页个数)
@router.get("/", response_model=ResultPlusModel[List[StudentOut]], summary='查询所有学生(根据页码和每页个数)')
def read_students(db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
        查询所有学生(根据页码和每页个数)

        - pageIndex - 页码 (默认值 1)
        - pageSize - 每页个数 (默认值 10)
    """
    get_students = crud.student.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_students, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个学生信息.")


# 根据 id 查询学生信息
@router.get("/{id}", response_model=ResultModel[StudentOut], summary='根据 id 查询学生信息')
def read_student(db: Session = Depends(deps.get_db), id: int = None) -> Any:
    """
        根据 id 查询学生信息

        - id - 学号
    """
    get_student = crud.student.get(db, id=id)
    if not get_student:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的学生.")
    return resp_200(data=get_student, msg=f"查询到了 id 为 {id} 的学生.")


# 添加学生信息
@router.post("/", response_model=ResultModel[StudentOut], summary='添加学生信息')
def create_student(*, db: Session = Depends(deps.get_db), student_in: StudentCreate) -> Any:
    """ 添加学生信息(已添加异常捕获) """
    add_student = crud.student.create(db, obj_in=student_in)
    return resp_200(data=add_student, msg=f"添加了 id 为 {student_in.id} 的学生信息.")


# 通过 id 更新学生信息
@router.put("/{id}", response_model=ResultModel[StudentOut], summary='通过 id 更新学生信息')
def update_student(*, db: Session = Depends(deps.get_db), id: int, student_in: StudentUpdate) -> Any:
    """ 通过 id 更新学生信息(已添加异常捕获) """
    get_student = crud.student.get(db, id=id)
    if not get_student:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的学生.")
    else:
        alter_student = crud.student.update(db, db_obj=get_student, obj_in=student_in)
        return resp_200(data=alter_student, msg=f"更新了 id 为 {id} 的学生信息.")


# 通过 id 删除学生信息
@router.delete("/{student_id}", response_model=ResultModel[StudentOut], summary='通过 id 删除学生信息')
def delete_student(*, db: Session = Depends(deps.get_db), student_id: int) -> Any:
    """ 通过 id 删除学生信息(已添加异常捕获) """
    del_student = crud.student.remove(db, id=student_id)
    return resp_200(data=del_student, msg=f"删除了 id 为 {student_id} 的学生信息.")


# 只获取关系字段
@router.get("/relation/", response_class=ORJSONResponse, summary='获取到 学生表 中的关系字段')
def get_student_relation(db: Session = Depends(deps.get_db)) -> Any:
    """ 只获取关系字段 """
    get_students = crud.student.get_multi_relation(db)
    return resp_200(data=get_students, msg="获取到 学生表 中的关系字段.")
