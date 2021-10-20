#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:01
# @Author : 小四先生
# @desc :
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.api import deps
from backend.core.config import logger

router = APIRouter()


# 查询所有用户
@router.get("/", response_model=List[schemas.User])
def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    查询从 skip 到 limit 的用户
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    logger.info(f"查询了从 {skip} 到 {limit} 之间的用户.")
    return users


# 通过 id 查询用户
@router.get("/{user_id}", response_model=schemas.User)
def read_user(
        user_id: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    通过 id 查询用户
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        logger.warning(f"系统中不存在 id 为 {user_id} 的用户.")
        raise HTTPException(
            status_code=404,
            detail="系统中不存在此用户名的用户.",
        )
    logger.info(f"查询到了 id 为 {user_id} 的用户.")
    return user


# 添加用户信息
@router.post("/", response_model=schemas.User)
def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate,
) -> Any:
    """
    添加用户信息
    """
    user = crud.user.get(db, id=user_in.id)
    if user:
        logger.warning(f"系统中已经存在 id 为 {user_in.id} 的用户.")
        raise HTTPException(
            status_code=400,
            detail="系统中已经存在该用户名的用户.",
        )
    user = crud.user.create(db, obj_in=user_in)
    logger.info(f"添加了 id 为 {user_in.id} 的用户.")
    return user


# 通过 id 更新用户信息
@router.put("/{user_id}", response_model=schemas.User)
def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: int,
        user_in: schemas.UserUpdate,
) -> Any:
    """
    通过 id 更新用户信息
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        logger.warning(f"系统中不存在 id 为 {user_id} 的用户.")
        raise HTTPException(
            status_code=404,
            detail="系统中不存在此用户名的用户.",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    logger.info(f"更新了 id 为 {user_id} 的用户.")
    return user


# 通过 id 删除用户信息
@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: int
) -> Any:
    """
    通过 id 删除用户信息
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        logger.warning(f"系统中不存在 id 为 {user_id} 的用户.")
        raise HTTPException(
            status_code=404,
            detail="系统中不存在此用户名的用户.",
        )
    user = crud.user.remove(db, id=user_id)
    logger.info(f"删除了 id 为 {user_id} 的用户.")
    return user
