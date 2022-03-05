#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/17 15:15
# @Author : zxiaosi
# @desc : 管理员首页
import json
from typing import Any
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

import crud
from db import RedisPlus
from api.deps import get_redis, get_db, get_current_user
from models import Admin
from schemas import Todo, TodoId
from utils import resp_200

router = APIRouter()


@router.get("/dashboard/userInfo", response_class=ORJSONResponse, summary='查询了用户信息')
async def get_lang_todo(db: Session = Depends(get_db), current_user: Admin = Depends(get_current_user)) -> Any:
    """ 查询首页数据(用户信息) """
    user = crud.admin.get(db, id=current_user.id)
    return resp_200(data=user, msg='查询了用户信息')


@router.get("/dashboard/lang_todo_list", response_class=ORJSONResponse, summary='语言详情 && 待办事项')
async def get_lang_todo(redis: RedisPlus = Depends(get_redis)) -> Any:
    """ 查询首页数据(语言详情 && 待办事项) """
    language_details = await redis.list_loads('language_details')
    todo_list = await redis.list_loads('todo_list', 6)
    return resp_200(data={'todo_list': todo_list, 'language_details': language_details}, msg='查询了语言详情 && 待办事项')


@router.get("/dashboard/visit_todo_request", response_class=ORJSONResponse, summary='访问量 && 待办事项 && 请求数')
async def get_visit_todo_request(redis: RedisPlus = Depends(get_redis)) -> Any:
    """ 查询首页数据(访问量 && 待办事项 && 请求数) """
    visit_num = await redis.get('visit_num')
    todo_num = await redis.llen('todo_list')
    request_num = await redis.get('request_num')
    data = {'visit_num': visit_num, 'todo_num': todo_num, 'request_num': request_num}
    return resp_200(data=data, msg='查询了访问量 && 待办事项 && 请求数')


@router.post("/todo/add", response_class=ORJSONResponse, summary='添加待办')
async def add_todo(todo_in: Todo, redis: RedisPlus = Depends(get_redis)) -> Any:
    """ 添加待办 """
    text = {'title': todo_in.title, 'status': todo_in.status}
    await redis.cus_lpush('todo_list', text)
    todo_list = await redis.list_loads('todo_list', 6)
    todo_num = await redis.llen('todo_list')
    return resp_200(data={'todo_list': todo_list, 'todo_num': todo_num}, msg='添加待办成功！')


@router.post("/todo/update", response_class=ORJSONResponse, summary='根据索引更新待办')
async def update_todo(todo_in: TodoId, redis: RedisPlus = Depends(get_redis)) -> Any:
    """ 更新待办 """
    obj = await redis.get_list_by_index('todo_list', todo_in.id)
    obj["status"] = bool(1 - obj["status"])  # noqa 取反
    await redis.lset('todo_list', todo_in.id, json.dumps(obj))
    return resp_200(data=None, msg='更新待办成功！')
