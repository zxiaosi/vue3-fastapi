#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/17 15:15
# @Author : zxiaosi
# @desc : 首页
import json
from typing import Any
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from starlette.requests import Request

from utils import resp_200

router = APIRouter()

todoList = ['重构前端代码', '添加所有表信息', '调整代码结构', '添加学生表信息', '添加教师表信息']


# 查询首页数据
@router.get("/dashboard", response_class=ORJSONResponse, summary='查询首页数据')
async def get_dashboard(request: Request) -> Any:
    """ 查询首页数据 """
    request_num = await request.app.state.redis.get('request_num')
    todo_list = await request.app.state.mol_repo.list_loads('todo')
    return resp_200(data={'request_num': request_num, 'todoList': todo_list}, msg='查询首页数据')


# 添加待办 TODO 换成 hash
@router.post("/add/todo", response_class=ORJSONResponse, summary='添加待办')
async def add_todo(request: Request, todo_in: str) -> Any:
    """ 添加待办 """
    text = await request.app.state.mol_repo.dumps({'title': todo_in, 'status': False})
    await request.app.state.redis.lpush('todo', text)
    await request.app.state.redis.ltrim('todo', 0, 4)  # 裁剪[0, 4]之间的数据(左右为闭)
    todo_list = await request.app.state.mol_repo.list_loads('todo')
    return resp_200(data=todo_list, msg='添加成功！')


# 更新待办 TODO 换成 hash
@router.put("/update/todo", response_class=ORJSONResponse, summary='更新待办')
async def update_todo(request: Request, id: int = None) -> Any:
    """ 更新待办 """
    value = await request.app.state.redis.lrange('todo', 0, -1)
    text = await request.app.state.mol_repo.loads(value[id])
    text["status"] = bool(1 - text["status"])  # 布尔值取反
    test = await request.app.state.mol_repo.dumps(text)
    await request.app.state.redis.lset('todo', id, test)
    return resp_200(data=None, msg='更新成功！')
