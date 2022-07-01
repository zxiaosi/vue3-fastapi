#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:18
# @Author : zxiaosi
# @desc : 院系表接口
from typing import List

from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from schemas import DepartmentUpdate, DepartmentCreate, DepartmentOut as Department, Result, ResultPlus
from crud import department
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Department], summary='根据 id 查询院系信息')
async def read_department(id: int, db: AsyncSession = Depends(get_db),
                          user=Security(get_current_user, scopes=[])):
    _department = await department.get(db, id)
    if not _department:
        raise IdNotExist(f"系统中不存在 id 为 {id} 的院系.")
    return resp_200(data=_department, msg=f"查询到了 id 为 {id} 的院系.")


@router.get("/", response_model=ResultPlus[Department], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有院系')
async def read_departments(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                           user=Security(get_current_user, scopes=[])):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await department.get_number(db)
    _departments = await department.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _departments}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个院系信息.")


@router.post("/", response_model=Result, summary='添加院系信息')
async def create_department(department_in: DepartmentCreate, db: AsyncSession = Depends(get_db),
                            user=Security(get_current_user, scopes=["admin"])):
    await department.create(db, obj_in=department_in)
    return resp_200(msg=f"添加了 id 为 {department_in.id} 的院系信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新院系信息')
async def update_department(id: int, department_in: DepartmentUpdate, db: AsyncSession = Depends(get_db),
                            user=Security(get_current_user, scopes=["admin"])):
    rowcount = await department.update(db, id=id, obj_in=department_in)
    if not rowcount:  # 每次更新, 当前数据的更新时间会变, 只要id存在, 就会一直返回1
        raise IdNotExist(f"系统中不存在 id 为 {id} 的院系.")
    return resp_200(msg=f"更新了 id 为 {id} 的院系信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除院系信息')
async def delete_department(id: int, db: AsyncSession = Depends(get_db),
                            user=Security(get_current_user, scopes=["admin"])):
    rowcount = await department.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的院系.")
    return resp_200(msg=f'成功删除 id 为 {id} 的院系信息.')


@router.post("/del/", response_model=Result, summary='同时删除多个院系信息')
async def delete_departments(idList: List, db: AsyncSession = Depends(get_db),
                             user=Security(get_current_user, scopes=["admin"])):
    rowcount = await department.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个院系信息.')


@router.get("/sort/{name}", summary='根据字段排序')
async def get_select_courses(name: str, pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db)):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await department.get_number(db)
    _departments = await department.sort(db, name, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _departments}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个院系信息.")
