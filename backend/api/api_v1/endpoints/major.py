#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:17
# @Author : 小四先生
# @desc : 专业表接口
from typing import Any, List, Union, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from schemas import Major, MajorInDB, MajorCreate, MajorUpdate
from api import deps
from utils import RestfulModel, response

router = APIRouter()


# 查询所有专业 or 通过 id 查询专业信息
@router.get("/",
            response_model=RestfulModel[Union[Major, List[Major]]],
            summary='查询所有专业 or 通过 id 查询专业信息')
def read_majors(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        major_id: Optional[int] = None,  # 虽然是str类型,防止用户输入字符串
) -> Any:
    """
        查询从 skip 到 limit 的专业 || 通过 id 查询专业信息
        - skip - 起始
        - limit - 末尾
        - major_id - 专业编号
    """
    if major_id:
        get_major = crud.major.get(db, id=major_id)
        if not get_major:
            return response(code=404, msg=f"系统中不存在 id 为 {major_id} 的专业.")
        return response(msg=f"查询到了 id 为 {major_id} 的专业.", data=get_major)
    else:
        get_majors = crud.major.get_multi_by_department(db, skip=skip, limit=limit)
        return response(msg=f"查询了从 {skip} 到 {limit} 之间的专业.", data=get_majors)


# 添加专业信息
@router.post("/",
             response_model=RestfulModel[MajorInDB],
             summary='添加专业信息')
def create_major(
        *,
        db: Session = Depends(deps.get_db),
        major_in: MajorCreate,
) -> Any:
    """ 添加专业信息 """
    get_major = crud.major.get(db, id=major_in.id)
    if get_major:
        return response(code=400, msg=f"系统中已经存在 id 为 {major_in.id} 的专业.")
    else:
        if crud.department.get(db=db, id=major_in.department_id):
            add_major = crud.major.create(db, obj_in=major_in)
            return response(msg=f"添加了 id 为 {major_in.id} 的专业.", data=add_major)
        else:
            return response(code=404, msg=f"系统中不存在 id 为 {major_in.department_id} 的院系.")


# 通过 id 更新专业信息
@router.put("/{major_id}",
            response_model=RestfulModel[MajorInDB],
            summary='通过 id 更新专业信息')
def update_major(
        *,
        db: Session = Depends(deps.get_db),
        major_id: int,  # 防止用户输入字符串
        major_in: MajorUpdate,
) -> Any:
    """ 通过 id 更新专业信息 """
    get_major = crud.major.get(db, id=major_id)
    if not get_major:
        return response(code=404, msg=f"系统中不存在 id 为 {major_id} 的专业.")
    else:
        if crud.department.get(db=db, id=major_in.department_id):
            alter_major = crud.major.update(db, db_obj=get_major, obj_in=major_in)
            return response(msg=f"更新了 id 为 {major_id} 的专业信息.", data=alter_major)
        else:
            return response(code=404, msg=f"系统中不存在 id 为 {major_in.department_id} 的院系.")


# 通过 id 删除专业信息
@router.delete("/{major_id}",
               response_model=RestfulModel[MajorInDB],
               summary='通过 id 删除专业信息')
def delete_major(
        *,
        db: Session = Depends(deps.get_db),
        major_id: int  # 防止用户输入字符串
) -> Any:
    """ 通过 id 删除专业信息 """
    get_major = crud.major.get(db, id=major_id)
    if not get_major:
        return response(code=404, msg=f"系统中不存在 id 为 {major_id} 的专业.")
    del_major = crud.major.remove(db, id=major_id)
    return response(msg=f"删除了 id 为 {major_id} 的专业.", data=del_major)
