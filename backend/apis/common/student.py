#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:12
# @Author : zxiaosi
# @desc : 学生表接口
from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from schemas import StudentCreate, StudentUpdate, StudentOut as Student, Result, ResultPlus
from crud import student
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Student], summary='根据 id 查询学生信息')
async def read_student(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _student = await student.get(db, id)
    if not _student:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的学生.")
    return resp_200(data=_student, msg=f"查询到了 id 为 {id} 的学生.")


@router.get("/", response_model=ResultPlus[Student], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有学生')
async def read_students(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=[])):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await student.get_number(db)
    _students = await student.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _students}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个学生信息.")


@router.post("/", response_model=Result, summary='添加学生信息')
async def create_student(student_in: StudentCreate, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    await student.create(db, obj_in=student_in)
    return resp_200(msg=f"添加了 id 为 {student_in.id} 的学生信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新学生信息')
async def update_student(id: int, student_in: StudentUpdate, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    rowcount = await student.update(db, id=id, obj_in=student_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的学生.")
    return resp_200(msg=f"更新了 id 为 {id} 的学生信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除学生信息')
async def delete_student(id: int, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    rowcount = await student.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的学生.")
    return resp_200(msg=f"删除了 id 为 {id} 的学生信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个学生信息')
async def delete_students(idList: List, db: AsyncSession = Depends(get_db),
                          user=Security(get_current_user, scopes=['admin'])):
    rowcount = await student.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个学生信息.')


# @router.get("/detail/{id}", summary='得到详细信息')
# async def get_detail(id: int, db: AsyncSession = Depends(get_db)):
#     _data = await student.get_detail(db, id)
#     return _data
