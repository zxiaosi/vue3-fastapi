#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:25
# @Author : zxiaosi
# @desc : 选课表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api import deps
from schemas import SelectCourseCreate, SelectCourseUpdate, SelectCourseOut, ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有选课(根据页码和每页个数)
@router.get("/", response_model=ResultPlusModel[List[SelectCourseOut]], summary='查询所有选课(根据页码和每页个数)')
def read_select_courses(db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10) -> Any:
    """
        查询所有选课(根据页码和每页个数, pageIndex=-1&&pageSize=-1表示查询所有)

        - pageIndex - 页码 (默认值 1)
        - pageSize - 每页个数 (默认值 10)
    """
    get_select_courses = crud.selectCourse.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    if pageIndex == -1 and pageSize == -1:
        text = "查询了所有的选课信息."
    else:
        text = f"查询了第 {pageIndex} 页中的 {pageSize} 个选课信息."
    return resp_200(data=get_select_courses, msg=text)


# 根据 id 查询选课信息
@router.get("/{id}", response_model=ResultModel[SelectCourseOut], summary='根据 id 查询选课信息')
def read_select_course(db: Session = Depends(deps.get_db), id: int = None) -> Any:
    """
        根据 id 查询选课信息

        - id - 选课编号
    """
    get_select_course = crud.selectCourse.get(db, id=id)
    if not get_select_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    return resp_200(data=get_select_course, msg=f"查询到了 id 为 {id} 的选课.")


# 添加选课信息
@router.post("/", response_model=ResultModel[SelectCourseOut], summary='添加选课信息')
def create_select_course(*, db: Session = Depends(deps.get_db), select_course_in: SelectCourseCreate) -> Any:
    """ 添加选课信息(已添加异常捕获) """
    add_select_course = crud.selectCourse.create(db, obj_in=select_course_in)
    return resp_200(msg=f"添加了选课信息.", data=add_select_course)


# 通过 id 更新选课信息
@router.put("/{id}", response_model=ResultModel[SelectCourseOut], summary='通过 id 更新选课信息')
def update_select_course(*, db: Session = Depends(deps.get_db), id: int, select_course_in: SelectCourseUpdate) -> Any:
    """ 通过 id 更新选课信息(已添加异常捕获) """
    get_select_course = crud.selectCourse.get(db, id=id)
    if not get_select_course:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的选课.")
    else:
        alter_select_course = crud.selectCourse.update(db, db_obj=get_select_course, obj_in=select_course_in)
        return resp_200(data=alter_select_course, msg=f"更新了 id 为 {id} 的选课信息.")


# 通过 id 删除选课信息
@router.delete("/{id}", response_model=ResultModel[SelectCourseOut], summary='通过 id 删除选课信息')
def delete_select_course(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """ 通过 id 删除选课信息 """
    del_select_course = crud.selectCourse.remove(db, id=id)
    return resp_200(data=del_select_course, msg=f"删除了 id 为 {id} 的选课信息.")
