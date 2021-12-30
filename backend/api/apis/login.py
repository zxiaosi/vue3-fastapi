#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/28 19:16
# @Author : 小四先生
# @desc :
from datetime import timedelta
from typing import Any

from api import deps
from core import security
from core.config import settings
from core.security import get_password_hash
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import crud
import models
import schemas

router = APIRouter()


# 文档登录
@router.post("/login/access-token", response_model=schemas.Token, summary="用户登录认证")
def login_access_token(
        db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    兼容OAuth2的令牌登录，为将来的请求获取访问令牌
    """
    user = crud.user.authenticate(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="错误的用户名或密码！")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="当前用户未登录！")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
