#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 9:48
# @Author : zxiaosi
# @desc : 教师表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from schemas import TeacherOut, TeacherCreate, TeacherUpdate, Relation, ResultModel, ResultPlusModel
from crud import teacher
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/", response_model=ResultPlusModel[List[TeacherOut]], summary='查询所有教师(根据页码和每页个数)')
def read_teachers(db: Session = Depends(get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
    查询所有教师(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

    - pageIndex - 页码 (默认值 1)
    - pageSize - 每页个数 (默认值 10)
    """
    get_teachers = teacher.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_teachers, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个教师信息.")


@router.get("/{id}", response_model=ResultModel[TeacherOut], summary='根据 id 查询教师信息')
def read_teacher(db: Session = Depends(get_db), id: int = None) -> Any:
    get_teacher = teacher.get(db, id=id)
    if not get_teacher:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    return resp_200(data=get_teacher, msg=f"查询到了 id 为 {id} 的教师.")


@router.post("/", response_model=ResultModel[TeacherOut], summary='添加教师信息')
def create_teacher(*, db: Session = Depends(get_db), teacher_in: TeacherCreate) -> Any:
    add_teacher = teacher.create(db, obj_in=teacher_in)
    return resp_200(data=add_teacher, msg=f"添加了 id 为 {teacher_in.id} 的教师信息.")


@router.put("/{id}", response_model=ResultModel[TeacherOut], summary='通过 id 更新教师信息')
def update_teacher(*, db: Session = Depends(get_db), id: int, teacher_in: TeacherUpdate) -> Any:
    get_teacher = teacher.get(db, id=id)
    if not get_teacher:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    alter_teacher = teacher.update(db, db_obj=get_teacher, obj_in=teacher_in)
    return resp_200(data=alter_teacher, msg=f"更新了 id 为 {id} 的教师信息.")


@router.delete("/{id}", response_model=ResultModel[TeacherOut], summary='通过 id 删除教师信息')
def delete_teacher(*, db: Session = Depends(get_db), id: int) -> Any:
    del_teacher = teacher.remove(db, id=id)
    return resp_200(data=del_teacher, msg=f"删除了 id 为 {id} 的教师信息.")


@router.post("/del/", response_model=ResultModel, summary='同时删除多个教师信息')
def delete_teachers(*, db: Session = Depends(get_db), idList: list) -> Any:
    teacher.remove_multi(db, id_list=idList)
    return resp_200(data='', msg=f'成功删除多个院系信息.')


@router.get("/relation/", response_model=ResultPlusModel[List[Relation]], summary='获取到 教师表 中的关系字段')
def get_teacher_relation(db: Session = Depends(get_db)) -> Any:
    get_teachers = teacher.get_multi_relation(db)
    return resp_200(data=get_teachers, msg="获取到 教师表 中的关系字段.")
