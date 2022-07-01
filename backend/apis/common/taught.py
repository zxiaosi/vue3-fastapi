#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/5/10 21:08
# @Author : zxiaosi
# @desc : 讲授表接口
from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from models import Teacher
from schemas import TaughtCreate, TaughtUpdate, TaughtOut as Taught, Result, ResultPlus
from crud import taught
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Taught], summary='根据 id 查询讲授信息')
async def read_taught(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _taught = await taught.get(db, id)
    if not _taught:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的讲授.")
    return resp_200(data=_taught, msg=f"查询到了 id 为 {id} 的讲授.")


@router.get("/", response_model=ResultPlus[Taught], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有讲授')
async def read_taughts(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                       user=Security(get_current_user, scopes=[])):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await taught.get_number(db)
    _taughts = await taught.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _taughts}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个讲授信息.")


@router.post("/", response_model=Result, summary='添加讲授信息')
async def create_taught(taught_in: TaughtCreate, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=['admin'])):
    await taught.create(db, obj_in=taught_in)
    return resp_200(msg="添加了讲授信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新讲授信息')
async def update_taught(id: int, taught_in: TaughtUpdate, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=['admin'])):
    rowcount = await taught.update(db, id=id, obj_in=taught_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的讲授.")
    return resp_200(msg=f"更新了 id 为 {id} 的讲授信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除讲授信息')
async def delete_taught(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=['admin'])):
    rowcount = await taught.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的讲授.")
    return resp_200(msg=f"删除了 id 为 {id} 的讲授信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个讲授信息')
async def delete_taughts(idList: List, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    rowcount = await taught.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个讲授信息.')


@router.get("/detail/", response_model=Result, summary='获取教师讲授信息详情')
async def get_course_detail(db: AsyncSession = Depends(get_db), user: Teacher = Security(get_current_user, scopes=[])):
    data = await taught.get_course(db, id=user.id)
    return resp_200(data=data, msg='获取教师讲授信息详情.')
