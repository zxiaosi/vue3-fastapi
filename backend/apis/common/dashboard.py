#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/1/17 15:15
# @Author : zxiaosi
# @desc : 首页
import json
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from db import MyRedis
from apis.deps import get_redis
from schemas import Todo, TodoId
from utils import resp_200

router = APIRouter()


@router.get("/dashboard", response_class=ORJSONResponse, summary='访问量 && 待办数 && 请求数 && 待办事项')
async def get_visit_todo_request(redis: MyRedis = Depends(get_redis)):
    """ 查询首页数据(访问量 && 待办事项 && 请求数 && 待办事项) """
    visit_num = await redis.get('visit_num')
    todo_num = await redis.llen('todo_list')
    request_num = await redis.get('request_num')
    todo_list = await redis.list_loads('todo_list', 6)
    data = {'visit_num': visit_num, 'todo_num': todo_num, 'request_num': request_num, 'todo_list': todo_list}
    return resp_200(data=data, msg='查询了访问量 && 待办事项 && 请求数 && 待办事项')


@router.post("/todo/add", summary='添加待办')
async def add_todo(todo_in: Todo, redis: MyRedis = Depends(get_redis)):
    """ 添加待办 """
    text = {'title': todo_in.title, 'status': todo_in.status}
    await redis.cus_lpush('todo_list', text)
    return resp_200(msg='添加待办成功！')


@router.post("/todo/update", response_class=ORJSONResponse, summary='根据索引更新待办')
async def update_todo(todo_in: TodoId, redis: MyRedis = Depends(get_redis)):
    """ 更新待办 """
    obj = await redis.get_list_by_index('todo_list', todo_in.id)
    obj["status"] = bool(1 - obj["status"])  # noqa 取反
    await redis.lset('todo_list', todo_in.id, json.dumps(obj))
    return resp_200(msg='更新待办成功！')
