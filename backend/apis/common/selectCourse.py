#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:25
# @Author : zxiaosi
# @desc : 选课表接口
from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from schemas import SelectCourseCreate, SelectCourseUpdate, SelectCourse, Result, ResultPlus
from crud import selectCourse
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[SelectCourse], summary='根据 id 查询选课信息')
async def read_select_course(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _select_course = await selectCourse.get(db, id)
    if not _select_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(data=_select_course, msg=f"查询到了 id 为 {id} 的选课.")


@router.get("/", response_model=ResultPlus[SelectCourse], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有选课')
async def read_select_courses(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                              user=Security(get_current_user, scopes=[])):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await selectCourse.get_number(db)
    _select_courses = await selectCourse.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _select_courses}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个选课信息.")


@router.post("/", response_model=Result, summary='添加选课信息')
async def create_select_course(select_course_in: SelectCourseCreate, db: AsyncSession = Depends(get_db),
                               user=Security(get_current_user, scopes=['admin'])):
    await selectCourse.create(db, obj_in=select_course_in)
    return resp_200(msg="添加了选课信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新选课信息')
async def update_select_course(id: int, select_course_in: SelectCourseUpdate, db: AsyncSession = Depends(get_db),
                               user=Security(get_current_user, scopes=['admin'])):
    rowcount = await selectCourse.update(db, id=id, obj_in=select_course_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(msg=f"更新了 id 为 {id} 的选课信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除选课信息')
async def delete_select_course(id: int, db: AsyncSession = Depends(get_db),
                               user=Security(get_current_user, scopes=['admin'])):
    rowcount = await selectCourse.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(msg=f"删除了 id 为 {id} 的选课信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个选课信息')
async def delete_courses(idList: List, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=['admin'])):
    rowcount = await selectCourse.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个选课信息.')


@router.get("/get/", summary='根据页码 pageIndex 和每页个数 pageSize 查询所有选课')
async def get_select_courses(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db)):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await selectCourse.get_number(db)
    _select_courses = await selectCourse.get_multi_id_name(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _select_courses}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个选课信息.")
