#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 16:42
# @Author : zxiaosi
# @desc : 课程表接口
from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from schemas import CourseCreate, CourseUpdate, CourseOut as Course, Result, ResultPlus
from crud import course
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Course], summary='根据 id 查询课程信息')
async def read_course(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _course = await course.get(db, id)
    if not _course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    return resp_200(data=_course, msg=f"查询到了 id 为 {id} 的课程.")


@router.get("/", response_model=ResultPlus[Course], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有课程')
async def read_courses(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                       user=Security(get_current_user, scopes=[])):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await course.get_number(db)
    _courses = await course.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _courses}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个课程信息.")


@router.post("/", response_model=Result, summary='添加课程信息')
async def create_course(course_in: CourseCreate, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=["admin"])):
    await course.create(db, obj_in=course_in)
    return resp_200(msg=f"添加了 id 为 {course_in.id} 的课程信息.")


@router.put("/{id}", response_model=Result, summary='通过 id 更新课程信息')
async def update_course(id: int, course_in: CourseUpdate, db: AsyncSession = Depends(get_db),
                        user=Security(get_current_user, scopes=["admin"])):
    rowcount = await course.update(db, id=id, obj_in=course_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    return resp_200(msg=f"更新了 id 为 {id} 的课程信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除课程信息')
async def delete_course(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=["admin"])):
    rowcount = await course.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的课程.")
    return resp_200(msg=f"删除了 id 为 {id} 的课程信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个课程信息')
async def delete_courses(idList: List, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=["admin"])):
    rowcount = await course.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个课程信息.')
