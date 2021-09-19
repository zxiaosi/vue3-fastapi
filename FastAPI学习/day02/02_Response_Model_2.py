#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/9 10:15
# @Author : 小四先生
# @desc :
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


# Don't do this in production!
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
