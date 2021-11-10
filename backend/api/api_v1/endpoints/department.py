#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:18
# @Author : 小四先生
# @desc : 院系表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from api import deps
from core.logger import logger

router = APIRouter()


# 查询所有院系 or 根据 id 查询院系信息
@router.get("/",
            response_model=Union[schemas.Department, List[schemas.Department]],
            summary='查询所有院系 or 根据 id 查询院系信息')
def read_departments(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        departments_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """ 查询从 skip 到 limit 的院系 || 根据 id 查询院系信息 """
    if departments_id:  # 查询从 skip 到 limit 的院系
        department = crud.department.get(db, id=departments_id)
        if not department:
            logger.warning(f"系统中不存在 id 为 {departments_id} 的院系.")
            raise HTTPException(status_code=404, detail=f"系统中不存在 id 为 {departments_id} 的院系.")
        logger.info(f"查询到了 id 为 {departments_id} 的院系.")
        return department
    else:  # 根据 id 查询院系信息
        departments = crud.department.get_multi(db, skip=skip, limit=limit)
        logger.info(f"查询了从 {skip} 到 {limit} 之间的院系.")
        return departments


# 添加院系信息
@router.post("/", response_model=schemas.Department, summary='添加院系信息')
def create_department(
        *,
        db: Session = Depends(deps.get_db),
        department_in: schemas.DepartmentCreate,
) -> Any:
    """ 添加院系信息 """
    department = crud.department.get(db, id=department_in.id)
    if department:
        logger.warning(f"系统中已经存在 id 为 {department_in.id} 的院系.")
        raise HTTPException(status_code=400, detail=f"系统中已经存在 id 为 {department_in.id} 的院系.")
    department = crud.department.create(db, obj_in=department_in)
    logger.info(f"添加了 id 为 {department_in.id} 的院系.")
    return department


# 通过 id 更新院系信息
@router.put("/{department_id}", response_model=schemas.Department, summary='通过 id 更新院系信息')
def update_department(
        *,
        db: Session = Depends(deps.get_db),
        department_id: int,  # 防止用户输入字符串
        department_in: schemas.DepartmentUpdate,
) -> Any:
    """ 通过 id 更新院系信息 """
    department = crud.department.get(db, id=department_id)
    if not department:
        logger.warning(f"系统中不存在 id 为 {department_id} 的院系.")
        raise HTTPException(status_code=404, detail=f"系统中不存在 id 为 {department_id} 的院系.")
    department = crud.department.update(db, db_obj=department, obj_in=department_in)
    logger.info(f"更新了 id 为 {department_id} 的院系信息.")
    return department


# 通过 id 删除院系信息
@router.delete("/{department_id}", response_model=schemas.Msg, summary='通过 id 删除院系信息')
def delete_department(
        *,
        db: Session = Depends(deps.get_db),
        department_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除院系信息 """
    department = crud.department.get(db, id=department_id)
    if not department:
        logger.warning(f"系统中不存在 id 为 {department_id} 的院系.")
        raise HTTPException(status_code=404, detail=f"系统中不存在 id 为 {department_id} 的院系.")
    crud.department.remove(db, id=department_id)
    logger.info(f"删除了 id 为 {department_id} 的院系.")
    return {'msg': f'成功删除 id 为 {department_id} 的院系'}
