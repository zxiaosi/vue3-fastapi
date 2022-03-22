#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:17
# @Author : zxiaosi
# @desc : 专业表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from schemas import MajorCreate, MajorUpdate, MajorOut, Relation, ResultModel, ResultPlusModel
from crud import major
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/", response_model=ResultPlusModel[List[MajorOut]], summary='查询所有专业(根据页码和每页个数)')
def read_majors(db: Session = Depends(get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
    查询所有专业(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

    - pageIndex - 页码 (默认值 1)
    - pageSize - 每页个数 (默认值 10)
    """
    get_majors = major.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_majors, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个专业信息.")


@router.get("/{id}", response_model=ResultModel[MajorOut], summary='根据 id 查询专业信息')
def read_major(db: Session = Depends(get_db), id: int = None) -> Any:
    get_major = major.get(db, id=id)
    if not get_major:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的专业.")
    return resp_200(data=get_major, msg=f"查询到了 id 为 {id} 的专业.")


@router.post("/", response_model=ResultModel[MajorOut], summary='添加专业信息')
def create_major(*, db: Session = Depends(get_db), major_in: MajorCreate) -> Any:
    add_major = major.create(db, obj_in=major_in)
    return resp_200(data=add_major, msg=f"添加了 id 为 {major_in.id} 的专业信息.")


@router.put("/{id}", response_model=ResultModel[MajorOut], summary='通过 id 更新专业信息')
def update_major(*, db: Session = Depends(get_db), id: int, major_in: MajorUpdate) -> Any:
    get_major = major.get(db, id=id)
    if not get_major:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的专业.")
    alter_major = major.update(db, db_obj=get_major, obj_in=major_in)
    return resp_200(data=alter_major, msg=f"更新了 id 为 {id} 的专业信息.")


@router.delete("/{id}", response_model=ResultModel[MajorOut], summary='通过 id 删除专业信息')
def delete_major(*, db: Session = Depends(get_db), id: int) -> Any:
    del_major = major.remove(db, id=id)
    return resp_200(data=del_major, msg=f"删除了 id 为 {id} 的专业信息.")


@router.post("/del/", response_model=ResultModel, summary='同时删除多个专业信息')
def delete_majors(*, db: Session = Depends(get_db), idList: list) -> Any:
    major.remove_multi(db, id_list=idList)
    return resp_200(data='', msg=f'同时删除多个专业信息.')


@router.get("/relation/", response_model=ResultPlusModel[List[Relation]], summary='获取到 专业表 中的关系字段')
def get_major_relation(db: Session = Depends(get_db)) -> Any:
    get_majors = major.get_multi_relation(db)
    return resp_200(data=get_majors, msg="获取到 专业表 中的关系字段.")
