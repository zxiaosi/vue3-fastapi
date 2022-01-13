#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:18
# @Author : zxiaosi
# @desc : 院系表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import DepartmentUpdate, DepartmentCreate, DepartmentOut, ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有院系(根据页码和每页个数)
@router.get("/", response_model=ResultPlusModel[List[DepartmentOut]], summary='查询所有院系(根据页码和每页个数)')
def read_departments(db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
        查询所有院系(根据页码和每页个数)

        - pageIndex - 页码 (默认值 1)
        - pageSize - 每页个数 (默认值 10)
    """
    get_departments = crud.department.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_departments, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个院系信息.")


# 根据 id 查询院系信息
@router.get("/{id}", response_model=ResultModel[DepartmentOut], summary='根据 id 查询院系信息')
def read_department(db: Session = Depends(deps.get_db), id: int = None) -> Any:  # 整型,防止用户输入字符串
    """
        根据 id 查询院系信息

        - id - 院系编号
    """
    get_department = crud.department.get(db, id=id)
    if not get_department:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的院系.")
    return resp_200(data=get_department, msg=f"查询到了 id 为 {id} 的院系.")


# 添加院系信息
@router.post("/", response_model=ResultModel[DepartmentOut], summary='添加院系信息')
def create_department(*, db: Session = Depends(deps.get_db), department_in: DepartmentCreate) -> Any:
    """ 添加院系信息(已添加异常捕获) """
    add_department = crud.department.create(db, obj_in=department_in)
    return resp_200(data=add_department, msg=f"添加了 id 为 {department_in.id} 的院系信息.")


# 通过 id 更新院系信息
@router.put("/{id}", response_model=ResultModel[DepartmentOut], summary='通过 id 更新院系信息')
def update_department(*, db: Session = Depends(deps.get_db), id: int, department_in: DepartmentUpdate) -> Any:
    """ 通过 id 更新院系信息(已添加异常捕获) """
    get_department = crud.department.get(db, id=id)
    if not get_department:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的院系.")
    alter_department = crud.department.update(db, db_obj=get_department, obj_in=department_in)
    return resp_200(data=alter_department, msg=f"更新了 id 为 {id} 的院系信息.")


# 通过 id 删除院系信息
@router.delete("/{id}", response_model=ResultModel[DepartmentOut], summary='通过 id 删除院系信息')
def delete_department(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """ 通过 id 删除院系信息(已添加异常捕获) """
    del_department = crud.department.remove(db, id=id)
    return resp_200(data=del_department, msg=f'成功删除 id 为 {id} 的院系信息.')
