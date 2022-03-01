#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/28 19:16
# @Author : zxiaosi
# @desc : 登录
import json
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

import crud
from core import settings, create_access_token
from db import RedisPlus
from models import Admin
from schemas import ResultModel, Token, AdminOut, Login, Logout
from api.deps import get_redis, get_db, get_current_user
from utils import resp_200, SetRedis, ErrorUser

router = APIRouter()


@router.post("/login/access-token", response_model=Token, summary="docs接口文档登录")
async def login_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    兼容OAuth2的令牌登录，为接口文档的请求获取访问令牌
    - username: admin
    - password: 123
    """
    user = crud.admin.authenticate(db, username=form_data.username, password=form_data.password)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.id, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}  # 这里返回的格式一定这么写,否则get_current_user依赖拿不到token


@router.post("/login/test-token", response_model=ResultModel[AdminOut], summary="获取当前用户")
def test_token(current_user: Admin = Depends(get_current_user)):
    return resp_200(data=jsonable_encoder(current_user), msg='获取到了当前用户信息！')


@router.post("/login", response_model=ResultModel[Token], summary="登录接口(已隐藏)", include_in_schema=False)
async def login_access_token(form_data: Login, db: Session = Depends(get_db), redis: RedisPlus = Depends(get_redis)):
    user = crud.admin.authenticate(db, username=form_data.username, password=form_data.password)
    if not user:
        raise ErrorUser('错误的用户名或密码!')

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.id, expires_delta=access_token_expires)

    try:
        await redis.set(name=token, value=json.dumps(jsonable_encoder(user)), ex=access_token_expires)
        return resp_200(data={"access_token": token, "token_type": "bearer"}, msg='登录成功！')
    except Exception as e:  # noqa: E722
        raise SetRedis(f'Redis存储 token 失败！--{e}')


@router.post("/logout", response_model=ResultModel, summary="退出登录(已隐藏)", include_in_schema=False)
async def logout_token(request: Request, redis: RedisPlus = Depends(get_redis)):
    await redis.delete(request.headers['authorization'])
    return resp_200(data='', msg='退出登录')
