#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:25
# @Author : zxiaosi
# @desc : 选课表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db, get_current_user
from models import Admin
from schemas import SelectCourseCreate, SelectCourseUpdate, SelectCourseOut, Relation, ResultModel, ResultPlusModel
from crud import selectCourse
from utils import resp_200, IdNotExist

router = APIRouter()


@router.get("/", response_model=ResultPlusModel[List[SelectCourseOut]], summary='查询所有选课(根据页码和每页个数)')
def read_select_courses(
        db: Session = Depends(get_db),
        pageIndex: int = 1,
        pageSize: int = 10,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    """
    查询所有选课(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

    - pageIndex - 页码 (默认值 1)
    - pageSize - 每页个数 (默认值 10)
    """
    get_select_courses = selectCourse.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=get_select_courses, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个选课信息.")


@router.get("/{id}", response_model=ResultModel[SelectCourseOut], summary='根据 id 查询选课信息')
def read_select_course(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    get_select_course = selectCourse.get(db, id=id)
    if not get_select_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(data=get_select_course, msg=f"查询到了 id 为 {id} 的选课.")


@router.post("/", response_model=ResultModel[SelectCourseOut], summary='添加选课信息')
def create_select_course(
        *,
        db: Session = Depends(get_db),
        select_course_in: SelectCourseCreate,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    add_select_course = selectCourse.create(db, obj_in=select_course_in)
    return resp_200(msg=f"添加了选课信息.", data=add_select_course)


@router.put("/{id}", response_model=ResultModel[SelectCourseOut], summary='通过 id 更新选课信息')
def update_select_course(
        *,
        db: Session = Depends(get_db),
        id: int,
        select_course_in: SelectCourseUpdate,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    get_select_course = selectCourse.get(db, id=id)
    if not get_select_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    alter_select_course = selectCourse.update(db, db_obj=get_select_course, obj_in=select_course_in)
    return resp_200(data=alter_select_course, msg=f"更新了 id 为 {id} 的选课信息.")


@router.delete("/{id}", response_model=ResultModel[SelectCourseOut], summary='通过 id 删除选课信息')
def delete_select_course(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    del_select_course = selectCourse.remove(db, id=id)
    return resp_200(data=del_select_course, msg=f"删除了 id 为 {id} 的选课信息.")


@router.post("/del/", response_model=ResultModel[Relation], summary='同时删除多个选课信息')
def select_select_courses(
        *,
        db: Session = Depends(get_db),
        idList: list,
        current_user: Admin = Depends(get_current_user)
) -> Any:
    selectCourse.remove_multi(db, id_list=idList)
    return resp_200(msg=f'同时删除多个选课信息.')
