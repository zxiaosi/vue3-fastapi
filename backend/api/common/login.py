#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/28 19:16
# @Author : zxiaosi
# @desc : 登录
import json
from datetime import timedelta
from ipaddress import ip_address

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

import crud
from core import settings, create_access_token
from db import RedisPlus
from models import Admin
from schemas import ResultModel, Token, AdminOut
from api.deps import get_redis, get_db, get_current_user
from utils import resp_200, SetRedis, ErrorUser, by_ip_get_address

router = APIRouter()


# 这里的登录借助的是OAuth2,与redis存储的token已经没有关系 (前端请求要发送 表单请求)
# OAuth2中token过期时间与 设置的时间 以及 服务的开启关闭 有关, 时间到期或者服务关闭token过期
@router.post("/login", response_model=Token, summary="docs接口文档登录 && 登录接口")
async def login_access_token(
        request: Request,
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    兼容OAuth2的令牌登录，为接口文档的请求获取访问令牌
    - username: admin
    - password: 123
    """
    user = crud.admin.authenticate(db, username=form_data.username, password=form_data.password)
    if not user:
        raise ErrorUser('错误的用户名或密码!')

    address = by_ip_get_address(request.client.host)  # 根据ip获取地址
    crud.admin.update(db, db_obj=user, obj_in={'address': address, 'password': ''})

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.id, expires_delta=access_token_expires)

    if not request.headers.get('referer').endswith('docs'):  # True: 前端接口 | False: 文档登录
        try:
            await request.app.state.redis.incr('visit_num')  # 用户访问量 自增1
            await request.app.state.redis.set(token, json.dumps(jsonable_encoder(user)), access_token_expires)
        except Exception as e:
            raise SetRedis(f'Redis存储 token 失败！-- {e}')

    return {"access_token": token, "token_type": "bearer"}  # 这里返回的格式一定这么写,否则get_current_user依赖拿不到token


@router.post("/login/current_user", response_model=ResultModel[AdminOut], summary="获取当前用户")
def get_current_user(current_user: Admin = Depends(get_current_user)):
    return resp_200(data=jsonable_encoder(current_user), msg='获取到了当前用户信息！')


@router.post("/logout", response_model=ResultModel, summary="退出登录(已隐藏)", include_in_schema=False)
async def logout_token(request: Request, redis: RedisPlus = Depends(get_redis)):
    token = request.headers.get('authorization')[7:]  # 去除token前面的 Bearer
    await redis.delete(token)
    return resp_200(data='', msg='退出登录')
