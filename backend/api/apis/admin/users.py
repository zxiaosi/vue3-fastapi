#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : zxiaosi
# @desc : 用户表接口
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
import models
from api import deps
from schemas import ResultModel, ResultPlusModel
from utils import resp_200, IdNotExist

router = APIRouter()


# 查询所有用户
@router.get("/", response_model=ResultPlusModel[List[schemas.User]])
def read_users(
        db: Session = Depends(deps.get_db), pageIndex: int = 1, pageSize: int = 10,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """查询所有用户(根据页码和每页个数)"""
    users = crud.user.get_multi(db, pageIndex=pageIndex, pageSize=pageSize)
    return resp_200(data=users, msg=f"查询了第 {pageIndex} 页中的 {pageSize} 个用户信息.")


# 通过 id 查询用户
@router.get("/{id}", response_model=ResultModel[schemas.User])
def read_user(
        db: Session = Depends(deps.get_db), id: int = None,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """通过 id 查询用户"""
    user = crud.user.get(db, id=id)
    if not user:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的用户.")
    return resp_200(data=user, msg=f"查询到了 id 为 {id} 的用户.")


# 添加用户信息
@router.post("/", response_model=ResultModel[schemas.User])
def create_user(
        *, db: Session = Depends(deps.get_db), user_in: schemas.UserCreate,
        # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """添加用户信息"""
    user = crud.user.create(db, obj_in=user_in)
    return resp_200(data=user, msg=f"添加了 id 为 {user_in.id} 的用户.")


# 通过 id 更新用户信息
@router.put("/{id}", response_model=ResultModel[schemas.User])
def update_user(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        user_in: schemas.UserUpdate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    通过 id 更新用户信息
    """
    user = crud.user.get(db, id=id)
    if not user:
        raise IdNotExist(err_desc=f"系统中不存在 id 为 {id} 的用户.")
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return resp_200(data=user, msg=f"更新了 id 为 {id} 的用户信息.")


# 通过 id 删除用户信息
@router.delete("/{id}", response_model=ResultModel[schemas.User])
def delete_user(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """通过 id 删除用户信息"""
    user = crud.user.remove(db, id=id)
    return resp_200(data=user, msg=f'成功删除 id 为 {id} 的用户信息.')
