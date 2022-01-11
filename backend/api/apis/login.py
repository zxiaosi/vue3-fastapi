#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/28 19:16
# @Author : zxiaosi
# @desc : 登录 TODO
import json
from typing import Any
from datetime import timedelta
from starlette.requests import Request
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

import crud
import models
import schemas
from api import deps
from core import settings, create_access_token
from sqlalchemy.orm import Session
from utils.logger import logger

router = APIRouter()


# 文档登录
@router.post("/login/access-token", response_model=schemas.Token, summary="用户登录认证")
async def login_access_token(
        request: Request,
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """ 兼容OAuth2的令牌登录，为将来的请求获取访问令牌 """
    user = crud.user.authenticate(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="错误的用户名或密码！")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="当前用户未登录！")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.id, expires_delta=access_token_expires)
    try:
        await request.app.state.redis.set(user.full_name,
                                          json.dumps({'user': user.full_name, 'token': token}),
                                          access_token_expires)
        logger.info("存储token成功！！！")
        test = await request.app.state.redis.get(user.full_name)
        logger.info("token为 {}", json.loads(test)["token"])
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:  # noqa: E722
        print(e)
        logger.error("对不起,不能打开Redis！！！")


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """ 测试token """
    return current_user
