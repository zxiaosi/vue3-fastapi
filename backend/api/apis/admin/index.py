#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/17 15:15
# @Author : zxiaosi
# @desc : 首页
from typing import Any
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from starlette.requests import Request

from utils import resp_200

router = APIRouter()

language = [
    {'title': 'Vue', 'percentage': 44.3, 'color': '#42b983'},
    {'title': 'Python', 'percentage': 45.4, 'color': '#f1e05a'},
    {'title': 'JavaScript', 'percentage': 8.7, 'color': '#409EFF'},
    {'title': '其他', 'percentage': 1.6, 'color': '#f56c6c'},
]


# 查询首页数据
@router.get("/dashboard", response_class=ORJSONResponse, summary='查询首页数据')
async def get_dashboard(request: Request) -> Any:
    """ 查询首页数据 """
    request_num = await request.app.state.redis.get('request_num')
    language_details = await request.app.state.mol_repo.list_loads('language_details')
    todo_list = await request.app.state.mol_repo.list_loads('todo_list', 6)
    todo_num = await request.app.state.redis.llen('todo_list')
    return resp_200(data={'request_num': request_num,
                          'todo': {'list': todo_list, 'num': todo_num},
                          'language_details': language_details},
                    msg='查询首页数据')


# 添加待办
@router.post("/add/todo", response_class=ORJSONResponse, summary='添加待办')
async def add_todo(request: Request, todo_in: str) -> Any:
    """ 添加待办 """
    text = {'title': todo_in, 'status': False}
    await request.app.state.mol_repo.lpush('todo_list', text)
    todo_list = await request.app.state.mol_repo.list_loads('todo_list', 6)
    todo_num = await request.app.state.redis.llen('todo_list')
    return resp_200(data={'todo_list': todo_list, 'todo_num': todo_num}, msg='添加待办成功！')


# 更新待办
@router.put("/update/todo", response_class=ORJSONResponse, summary='更新待办')
async def update_todo(request: Request, id: int = None) -> Any:
    """ 更新待办 """
    obj = await request.app.state.mol_repo.get_list_by_index('todo_list', id)
    obj["status"] = bool(1 - obj["status"])  # 取反
    text = await request.app.state.mol_repo.dumps(obj)
    await request.app.state.redis.lset('todo_list', id, text)
    return resp_200(data=None, msg='更新待办成功！')
