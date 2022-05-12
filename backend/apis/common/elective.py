#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:25
# @Author : zxiaosi
# @desc : 选课表接口
from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from apis.deps import get_db, get_current_user
from models import Student
from schemas import ElectiveCreate, ElectiveUpdate, ElectiveOut as Elective, Result, ResultPlus
from crud import elective
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/{id}", response_model=Result[Elective], summary='根据 id 查询选课信息')
async def read_elective(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    _elective = await elective.get(db, id)
    if not _elective:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(data=_elective, msg=f"查询到了 id 为 {id} 的选课.")


@router.get("/", response_model=ResultPlus[Elective], summary='根据页码 pageIndex 和每页个数 pageSize 查询所有选课')
async def read_electives(pageIndex: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db),
                         user=Security(get_current_user, scopes=[])):
    """ 查询所有院系 (pageIndex = -1 && pageSize = -1 表示查询所有) """
    _count = await elective.get_number(db)
    _electives = await elective.get_multi(db, pageIndex, pageSize)
    return resp_200(data={"count": _count, "list": _electives}, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个选课信息.")


@router.post("/", response_model=Result, summary='添加选课信息')
async def create_elective(elective_in: ElectiveCreate, db: AsyncSession = Depends(get_db),
                          user=Security(get_current_user, scopes=[])):
    await elective.create(db, obj_in=elective_in)
    return resp_200(msg='添加了选课信息.')


@router.put("/{id}", response_model=Result, summary='通过 id 更新选课信息')
async def update_elective(id: int, elective_in: ElectiveUpdate, db: AsyncSession = Depends(get_db),
                          user=Security(get_current_user, scopes=[])):
    rowcount = await elective.update(db, id=id, obj_in=elective_in)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(msg=f"更新了 id 为 {id} 的选课信息.")


@router.delete("/{id}", response_model=Result, summary='通过 id 删除选课信息')
async def delete_elective(id: int, db: AsyncSession = Depends(get_db), user=Security(get_current_user, scopes=[])):
    rowcount = await elective.remove(db, id)
    if not rowcount:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(msg=f"删除了 id 为 {id} 的选课信息.")


@router.post("/del/", response_model=Result, summary='同时删除多个选课信息')
async def delete_electives(idList: List, db: AsyncSession = Depends(get_db),
                           user=Security(get_current_user, scopes=[])):
    rowcount = await elective.remove_multi(db, id_list=idList)
    if not rowcount:
        raise IdNotExist(err_desc="系统中不存在列表中的id.")
    return resp_200(msg='成功删除多个选课信息.')


@router.post("/add/{courseId}", response_model=Result, summary='添加选课信息')
async def create_elective_by_course_id(courseId: int, db: AsyncSession = Depends(get_db),
                                       user: Student = Security(get_current_user, scopes=[])):
    obj = await elective.is_exist(db, courseId=courseId, studentId=user.id)
    if obj:
        data, msg = 0, '数据已存在.'
    else:
        data, msg = 1, '添加了选课信息.'
        await elective.create(db, obj_in={'grade': 0, 'studentId': user.id, 'courseId': courseId})
    return resp_200(data=data, msg=msg)


@router.post("/del/{courseId}", response_model=Result, summary='通过其他字段删除选课信息')
async def del_elective_by_filed(courseId: int, db: AsyncSession = Depends(get_db),
                                user: Student = Security(get_current_user, scopes=[])):
    obj = await elective.is_exist(db, courseId=courseId, studentId=user.id)
    if obj:
        data, msg = 1, '数据存在, 退课成功'
        rowcount = await elective.remove(db, id=obj.id)
        if not rowcount:
            raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    else:
        data, msg = 0, '数据不存在, 退课失败！'
    return resp_200(data=data, msg=msg)


@router.get("/detail/", response_model=Result, summary='获取学生选课信息详情')
async def get_course_detail(db: AsyncSession = Depends(get_db), user: Student = Security(get_current_user, scopes=[])):
    data = await elective.get_course(db, id=user.id)
    return resp_200(data=data, msg='获取学生选课信息详情.')
