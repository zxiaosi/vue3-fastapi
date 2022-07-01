#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/12/28 19:16
# @Author : zxiaosi
# @desc : 登录
import json
from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Request, Security
from fastapi.security import OAuth2PasswordRequestForm

from core import settings, create_access_token
from db import MyRedis
from models import Admin, Teacher, Student
from schemas import Result, Token, AdminOut, TeacherOut, StudentOut
from apis.deps import get_redis, get_db, get_current_user
from utils import resp_200, SetRedis, ErrorUser, by_ip_get_address
from utils.permission_assign import by_scopes_get_crud

router = APIRouter()


# 用户登录推荐看一下这个库: https://fastapi-users.github.io/fastapi-users/
# 这里的登录借助的是OAuth2,存储用的JWT,与redis存储的token已经没有关系 (前端请求要发送 表单请求)
# OAuth2中token过期时间与 设置的时间 以及 服务的开启关闭 有关, 时间到期或者服务关闭token过期
@router.post("/login", response_model=Token, summary="docs接口文档登录 && 登录接口")
async def login_access_token(
        request: Request,
        db: AsyncSession = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    """ 兼容OAuth2的令牌登录，为接口文档的请求获取访问令牌 """
    crud_obj = by_scopes_get_crud(form_data.scopes)  # 权限分配
    _user = await crud_obj.authenticate(db, username=form_data.username, password=form_data.password)
    if not _user:
        raise ErrorUser()

    address = by_ip_get_address(request.client.host)  # 根据ip获取地址
    await crud_obj.update(db, id=_user.id, obj_in={'address': address})

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token({"sub": str(_user.id), "scopes": form_data.scopes}, access_token_expires)

    try:
        await request.app.state.redis.incr('visit_num')  # 用户访问量 自增1
        await request.app.state.redis.set(token, json.dumps(jsonable_encoder(_user)), access_token_expires)
    except Exception as e:
        raise SetRedis(f'Redis存储 token 失败！-- {e}')

    # 这里'access_token'和'token_type'一定要写,否则get_current_user依赖拿不到token
    # 可添加字段(先修改schemas/token里面的Token返回模型)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/admin/index", response_model=Result[AdminOut], summary="获取当前管理员")
def get_current_admin(current_user: Admin = Security(get_current_user, scopes=["admin"])):
    return resp_200(data=jsonable_encoder(current_user), msg='获取当前管理员信息！')


@router.get("/teacher/index", response_model=Result[TeacherOut], summary="获取当前教师")
def get_current_teacher(current_user: Teacher = Security(get_current_user, scopes=["teacher"])):
    return resp_200(data=jsonable_encoder(current_user), msg='获取当前教师信息！')


@router.get("/student/index", response_model=Result[StudentOut], summary="获取当前学生")
def get_current_student(current_user: Student = Security(get_current_user, scopes=["student"])):
    return resp_200(data=jsonable_encoder(current_user), msg='获取当前学生信息！')


@router.post("/logout", response_model=Result, summary="退出登录(已隐藏)", include_in_schema=False)
async def logout_token(request: Request, redis: MyRedis = Depends(get_redis)):
    if 'authorization' in request.headers.keys():
        token = request.headers.get('authorization')[7:]  # 去除token前面的 Bearer
        await redis.delete(token)
    return resp_200(msg='退出登录')
