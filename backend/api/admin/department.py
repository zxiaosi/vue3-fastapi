#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:18
# @Author : zxiaosi
# @desc : 院系表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db, get_current_user
from models import Admin
from schemas import DepartmentUpdate, DepartmentCreate, DepartmentOut, Relation, ResultModel, ResultPlusModel
from crud import department
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/", response_model=ResultPlusModel[List[DepartmentOut]], summary='查询所有院系(根据页码和每页个数)')
def read_departments(
        db: Session = Depends(get_db),
        pageIndex: int = 1,
        pageSize: int = 10,
        current_user: Admin = Depends(get_current_user)  # 检测 token
) -> Any:
    """
    查询所有院系(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

    - pageIndex - 页码 (默认值 1)
    - pageSize - 每页个数 (默认值 10)
    """
    get_departments = department.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_departments, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个院系信息.")


@router.get("/{id}", response_model=ResultModel[DepartmentOut], summary='根据 id 查询院系信息')
def read_department(*, db: Session = Depends(get_db), id: int, current_user: Admin = Depends(get_current_user)) -> Any:
    get_department = department.get(db, id=id)
    if not get_department:
        raise IdNotExist(f"系统中不存在 id 为 {id} 的院系.")
    return resp_200(data=get_department, msg=f"查询到了 id 为 {id} 的院系.")


@router.post("/", response_model=ResultModel[DepartmentOut], summary='添加院系信息')
def create_department(
        *,  # 加上*之后,默认参数与非默认参数位置不强制
        db: Session = Depends(get_db),
        department_in: DepartmentCreate,
        current_user: Admin = Depends(get_current_user)
):
    add_department = department.create(db, obj_in=department_in)
    return resp_200(data=add_department, msg=f"添加了 id 为 {department_in.id} 的院系信息.")


@router.put("/{id}", response_model=ResultModel[DepartmentOut], summary='通过 id 更新院系信息')
def update_department(
        *,
        db: Session = Depends(get_db),
        id: int,
        department_in: DepartmentUpdate,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    get_department = department.get(db, id=id)
    if not get_department:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的院系.")
    alter_department = department.update(db, db_obj=get_department, obj_in=department_in)
    return resp_200(data=alter_department, msg=f"更新了 id 为 {id} 的院系信息.")


@router.delete("/{id}", response_model=ResultModel[DepartmentOut], summary='通过 id 删除院系信息')
def delete_department(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    del_department = department.remove(db, id=id)
    return resp_200(data=del_department, msg=f'成功删除 id 为 {id} 的院系信息.')


@router.post("/del/", response_model=ResultModel, summary='同时删除多个院系信息')
def delete_departments(
        *,
        db: Session = Depends(get_db),
        idList: list,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    department.remove_multi(db, id_list=idList)
    return resp_200(data='', msg=f'成功删除多个院系信息.')


@router.get("/relation/", response_model=ResultModel[Relation], summary='获取到 院系表 中的关系字段')
def get_department_relation(db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)) -> Any:
    get_departments = department.get_multi_relation(db)
    return resp_200(data=get_departments, msg="获取到了 院系表 中的关系字段.")
