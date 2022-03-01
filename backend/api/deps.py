#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/15 20:10
# @Author : zxiaosi
# @desc : 依赖项
from typing import Generator
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette.requests import Request

from core import settings, check_jwt_token
from db import DBSession, RedisPlus
from schemas import TokenPayload
from crud import ModelType, admin
from utils import OperateDB, UserNotExist

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/login/access-token")


def get_db() -> Generator:
    """ 数据库连接对象 """
    with DBSession() as db:
        try:
            yield db
        except Exception as e:
            db.rollback()
            OperateDB(f"操作数据库出错--{e}")
        finally:
            db.close()


def get_redis(request: Request) -> RedisPlus:
    """ redis连接对象 """
    return request.app.state.redis


def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> ModelType:
    """ 得到当前用户(docs接口文档) """
    payload = check_jwt_token(token)
    token_data = TokenPayload(**payload)
    user = admin.get(db, id=token_data.sub)
    if not user:
        raise UserNotExist()
    return user


def get_current_active_user(current_user: ModelType = Depends(get_current_user)) -> ModelType:
    """ 得到当前登录用户 """
    if not admin.is_active_def(current_user):
        raise HTTPException(status_code=401, detail="用户未登录！！！")
    return current_user


def get_current_active_superuser(current_user: ModelType = Depends(get_current_user)) -> ModelType:
    """ 得到当前超级用户 """
    if not admin.is_superuser(current_user):
        raise HTTPException(status_code=401, detail="这个用户没有足够的权限！！！")
    return current_user
