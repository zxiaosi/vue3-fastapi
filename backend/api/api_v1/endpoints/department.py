#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:18
# @Author : 小四先生
# @desc : 院系表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from schemas import Department, DepartmentCreate, DepartmentInDB, DepartmentUpdate
from api import deps
from utils import RestfulModel, response

router = APIRouter()


# 查询所有院系 or 根据 id 查询院系信息
@router.get("/",
            response_model=RestfulModel[Union[Department, List[Department]]],
            summary='查询所有院系 or 根据 id 查询院系信息')
def read_departments(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        departments_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """
        查询从 skip 到 limit 的院系 || 根据 id 查询院系信息
        - skip - 起始
        - limit - 末尾
        - departments_id - 院系编号
    """
    if departments_id:  # 根据 id 查询院系信息
        get_department = crud.department.get(db, id=departments_id)
        if not get_department:
            return response(code=404, msg=f"系统中不存在 id 为 {departments_id} 的院系.")
        return response(msg=f"查询到了 id 为 {departments_id} 的院系.", data=get_department)
    else:  # 查询从 skip 到 limit 的院系
        get_departments = crud.department.get_multi(db, skip=skip, limit=limit)
        return response(msg=f"查询了从 {skip} 到 {limit} 之间的院系.", data=get_departments)


# 添加院系信息
@router.post("/",
             response_model=RestfulModel[DepartmentInDB],
             summary='添加院系信息')
def create_department(
        *,
        db: Session = Depends(deps.get_db),
        department_in: DepartmentCreate,
) -> Any:
    """ 添加院系信息 """
    get_department = crud.department.get(db, id=department_in.id)
    if get_department:
        return response(code=400, msg=f"系统中已经存在 id 为 {department_in.id} 的院系.")
    add_department = crud.department.create(db, obj_in=department_in)
    return response(msg=f"添加了 id 为 {department_in.id} 的院系.", data=add_department)


# 通过 id 更新院系信息
@router.put("/{department_id}",
            response_model=RestfulModel[DepartmentInDB],
            summary='通过 id 更新院系信息')
def update_department(
        *,
        db: Session = Depends(deps.get_db),
        department_id: int,  # 防止用户输入字符串
        department_in: DepartmentUpdate,
) -> Any:
    """ 通过 id 更新院系信息 """
    get_department = crud.department.get(db, id=department_id)
    if not get_department:
        return response(code=404, msg=f"系统中不存在 id 为 {department_id} 的院系.")
    alter_department = crud.department.update(db, db_obj=get_department, obj_in=department_in)
    return response(msg=f"更新了 id 为 {department_id} 的院系信息.", data=alter_department)


# 通过 id 删除院系信息
@router.delete("/{department_id}",
               response_model=RestfulModel[DepartmentInDB],
               summary='通过 id 删除院系信息')
def delete_department(
        *,
        db: Session = Depends(deps.get_db),
        department_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除院系信息 """
    get_department = crud.department.get(db, id=department_id)
    if not get_department:
        return response(code=404, msg=f"系统中不存在 id 为 {department_id} 的院系.")
    del_department = crud.department.remove(db, id=department_id)
    return response(msg=f'成功删除 id 为 {department_id} 的院系', data=del_department)
