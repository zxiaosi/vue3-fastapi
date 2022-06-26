#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/6/26 22:38
# @Author : zxiaosi
# @desc : 路由
from typing import List

from fastapi import HTTPException, APIRouter, Depends
from starlette.background import BackgroundTasks
from starlette.requests import Request
from tortoise.contrib.fastapi import HTTPNotFoundError

from deps import get_redis
from models import User_Pydantic, Users, UserIn_Pydantic, Status

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/users", response_model=List[User_Pydantic])
async def get_users():
    print(User_Pydantic)
    return await User_Pydantic.from_queryset(Users.all())


@router.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@router.put(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@router.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await Users.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")


@router.get("/health-check")
async def health_check(redis=Depends(get_redis)):
    try:
        # key:test:keys => key/test/keys
        value = await redis.get('request_num')
        await redis.set("request_num", int(value) + 1)
        msg = "开启Redis成功！！！"
    except Exception as e:  # noqa: E722
        value = 0
        msg = f"对不起,不能打开Redis!!! {e}"
    return {"request": f"总计请求次数 {value}", "msg": msg}
