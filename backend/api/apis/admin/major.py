#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:17
# @Author : zxiaosi
# @desc : 专业表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import MajorCreate, MajorUpdate, MajorOut, ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有专业(根据页码和每页个数)
@router.get("/", response_model=ResultPlusModel[List[MajorOut]], summary='查询所有专业(根据页码和每页个数)')
def read_majors(db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
        查询所有专业(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

        - pageIndex - 页码 (默认值 1)
        - pageSize - 每页个数 (默认值 10)
    """
    get_majors = crud.major.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    if pageIndex == -1 and pageSize == -1:
        text = "查询了所有的专业信息."
    else:
        text = f"查询了第 {pageIndex} 页中的 {pageSize} 个专业信息."
    return resp_200(data=get_majors, msg=text)


# 根据 id 查询专业信息
@router.get("/{id}", response_model=ResultModel[MajorOut], summary='根据 id 查询专业信息')
def read_major(db: Session = Depends(deps.get_db), id: int = None) -> Any:
    """
        根据 id 查询专业信息

        - id - 专业编号
    """
    get_major = crud.major.get(db, id=id)
    if not get_major:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的专业.")
    return resp_200(data=get_major, msg=f"查询到了 id 为 {id} 的专业.")


# 添加专业信息
@router.post("/", response_model=ResultModel[MajorOut], summary='添加专业信息')
def create_major(*, db: Session = Depends(deps.get_db), major_in: MajorCreate) -> Any:
    """ 添加专业信息(已添加异常捕获) """
    add_major = crud.major.create(db, obj_in=major_in)
    return resp_200(data=add_major, msg=f"添加了 id 为 {major_in.id} 的专业信息.")


# 通过 id 更新专业信息
@router.put("/{id}", response_model=ResultModel[MajorOut], summary='通过 id 更新专业信息')
def update_major(*, db: Session = Depends(deps.get_db), id: int, major_in: MajorUpdate) -> Any:
    """ 通过 id 更新专业信息(已添加异常捕获) """
    get_major = crud.major.get(db, id=id)
    if not get_major:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的专业.")
    else:
        alter_major = crud.major.update(db, db_obj=get_major, obj_in=major_in)
        return resp_200(data=alter_major, msg=f"更新了 id 为 {id} 的专业信息.")


# 通过 id 删除专业信息
@router.delete("/{id}", response_model=ResultModel[MajorOut], summary='通过 id 删除专业信息')
def delete_major(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """ 通过 id 删除专业信息(已添加异常捕获) """
    del_major = crud.major.remove(db, id=id)
    return resp_200(data=del_major, msg=f"删除了 id 为 {id} 的专业信息.")


# 只获取关系字段
@router.get("/relation/", response_class=ORJSONResponse, summary='获取到 专业表 中的关系字段')
def get_major_relation(db: Session = Depends(deps.get_db)) -> Any:
    """ 只获取关系字段 """
    get_majors = crud.major.get_multi_relation(db)
    return resp_200(data=get_majors, msg="获取到 专业表 中的关系字段.")
