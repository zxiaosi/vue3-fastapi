#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:17
# @Author : zxiaosi
# @desc : 专业表接口
from typing import List

from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from schemas import MajorCreate, MajorUpdate, MajorOut as Major, Result, ResultPlus
from crud import major
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Major], summary='根据 id 查询专业信息')
async def read_major(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _major = await major.get(db, id)
    if not _major:
        raise IdNotExist(f"系统中不存在 id 为 {id} 的专业.")
    return resp_200(data=_major, msg=f"查询到了 id 为 {id} 的专业.")


@router.get("/", response_model=ResultPlus[Major], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有专业')
async def read_majors(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                      user=Security(get_current_user, scopes=[])):
    """ 查询所有专业 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await major.get_number(db)
    _majors = await major.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _majors}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个专业信息.")


@router.post("/", response_model=Result, summary='添加专业信息')
async def create_major(major_in: MajorCreate, db: AsyncSession = Depends(get_db),
                       user=Security(get_current_user, scopes=["admin"])):
    await major.create(db, obj_in=major_in)
    return resp_200(msg=f"添加了 id 为 {major_in.id} 的专业信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新专业信息')
async def update_major(id: int, major_in: MajorUpdate, db: AsyncSession = Depends(get_db),
                       user=Security(get_current_user, scopes=["admin"])):
    rowcount = await major.update(db, id=id, obj_in=major_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的专业.")
    return resp_200(msg=f"更新了 id 为 {id} 的专业信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除专业信息')
async def delete_major(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=["admin"])):
    rowcount = await major.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的专业.")
    return resp_200(msg=f"删除了 id 为 {id} 的专业信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个专业信息')
async def delete_majors(idList: List, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=["admin"])):
    rowcount = await major.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='同时删除多个专业信息.')
