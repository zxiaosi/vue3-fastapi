#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/16 9:48
# @Author : zxiaosi
# @desc : 教师表接口
from typing import List

from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from schemas import TeacherCreate, TeacherUpdate, TeacherOut as Teacher, Result, ResultPlus
from crud import teacher
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Teacher], summary='根据 id 查询教师信息')
async def read_teacher(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _teacher = await teacher.get(db, id)
    if not _teacher:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    return resp_200(data=_teacher, msg=f"查询到了 id 为 {id} 的教师.")


@router.get("/", response_model=ResultPlus[Teacher], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有教师')
async def read_teachers(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=[])):
    """ 查询所有教师 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await teacher.get_number(db)
    _teachers = await teacher.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _teachers}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个教师信息.")


@router.post("/", response_model=Result, summary='添加教师信息')
async def create_teacher(teacher_in: TeacherCreate, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    await teacher.create(db, obj_in=teacher_in)
    return resp_200(msg=f"添加了 id 为 {teacher_in.id} 的教师信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新教师信息')
async def update_teacher(id: int, teacher_in: TeacherUpdate, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    rowcount = await teacher.update(db, id=id, obj_in=teacher_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    return resp_200(msg=f"更新了 id 为 {id} 的教师信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除教师信息')
async def delete_teacher(id: int, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    rowcount = await teacher.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的教师.")
    return resp_200(msg=f"删除了 id 为 {id} 的教师信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个教师信息')
async def delete_teachers(idList: List, db: AsyncSession = Depends(get_db),
                          user=Security(get_current_user, scopes=['admin'])):
    rowcount = await teacher.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个教师信息.')
