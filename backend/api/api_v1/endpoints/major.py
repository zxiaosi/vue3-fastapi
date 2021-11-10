#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:17
# @Author : 小四先生
# @desc : 专业表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from api import deps
from core.logger import logger

router = APIRouter()


# 查询所有专业 or 通过 id 查询专业信息
@router.get("/",
            response_model=Union[schemas.Major, List[schemas.Major]],
            # response_model_exclude={"department_id"},  # 除去 department_id 字段
            summary='查询所有专业 or 通过 id 查询专业信息')
def read_majors(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        major_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """ 查询从 skip 到 limit 的专业 || 通过 id 查询专业信息 """
    if major_id:
        major = crud.major.get(db, id=major_id)
        if not major:
            logger.warning(f"系统中不存在 id 为 {major_id} 的专业.")
            raise HTTPException(status_code=404, detail=f"系统中不存在 id 为 {major_id} 的专业.")
        logger.info(f"查询到了 id 为 {major_id} 的专业.")
        return major
    else:
        majors = crud.major.get_multi_by_department(db, skip=skip, limit=limit)
        logger.info(f"查询了从 {skip} 到 {limit} 之间的专业.")
        return majors


# 添加专业信息
@router.post("/", response_model=schemas.Major, summary='添加专业信息')
def create_major(
        *,
        db: Session = Depends(deps.get_db),
        major_in: schemas.MajorCreate,
) -> Any:
    """ 添加专业信息 """
    major = crud.major.get(db, id=major_in.id)
    if crud.department.get(db=db, id=major_in.department_id):
        if major:
            logger.warning(f"系统中已经存在 id 为 {major_in.id} 的专业.")
            raise HTTPException(status_code=400, detail=f"系统中已经存在 id 为 {major_in.id} 的专业.")
    else:
        logger.warning(f"系统中不存在 id 为 {major_in.department_id} 的院系.")
        raise HTTPException(status_code=400, detail=f"系统中不存在 id 为 {major_in.department_id} 的院系.")
    major = crud.major.create(db, obj_in=major_in)
    logger.info(f"添加了 id 为 {major_in.id} 的专业.")
    return major


# 通过 id 更新专业信息
@router.put("/{major_id}", response_model=schemas.Major, summary='通过 id 更新专业信息')
def update_major(
        *,
        db: Session = Depends(deps.get_db),
        major_id: int,  # 防止用户输入字符串
        major_in: schemas.MajorUpdate,
) -> Any:
    """ 通过 id 更新专业信息 """
    major = crud.major.get(db, id=major_id)
    if crud.department.get(db=db, id=major_in.department_id):
        if not major:
            logger.warning(f"系统中不存在 id 为 {major_id} 的专业.")
            raise HTTPException(status_code=404, detail=f"系统中不存在 id 为 {major_id} 的专业.")
    else:
        logger.warning(f"系统中不存在 id 为 {major_in.department_id} 的院系.")
        raise HTTPException(status_code=400, detail=f"系统中不存在 id 为 {major_in.department_id} 的院系.")
    major = crud.major.update(db, db_obj=major, obj_in=major_in)
    logger.info(f"更新了 id 为 {major_id} 的专业信息.")
    return major


# 通过 id 删除专业信息
@router.delete("/{major_id}", response_model=schemas.Msg, summary='通过 id 删除专业信息')
def delete_major(
        *,
        db: Session = Depends(deps.get_db),
        major_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除专业信息 """
    major = crud.major.get(db, id=major_id)
    if not major:
        logger.warning(f"系统中不存在 id 为 {major_id} 的专业.")
        raise HTTPException(status_code=404, detail=f"系统中不存在 id 为 {major_id} 的专业.")
    crud.major.remove(db, id=major_id)
    logger.info(f"删除了 id 为 {major_id} 的专业.")
    return {'msg': f'成功删除 id 为 {major_id} 的专业!'}
