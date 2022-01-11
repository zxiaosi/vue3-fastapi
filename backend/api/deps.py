#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:10
# @Author : zxiaosi
# @desc : 获取数据库连接对象 TODO
from jose import jwt
from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session

import crud
import models
import schemas
from core import settings, ALGORITHM
from db import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_STR}/login/access-token")


# 数据库连接对象
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 得到当前用户
def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 得到当前登录用户
def get_current_active_user(current_user: models.User = Depends(get_current_user)) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=401, detail="用户未登录！！！")
    return current_user


# 得到当前超级用户
def get_current_active_superuser(current_user: models.User = Depends(get_current_user)) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=401, detail="这个用户没有足够的权限！！！")
    return current_user
