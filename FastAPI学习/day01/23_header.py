#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 15:23
# @Author : 小四先生
# @desc :
from typing import Optional
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None), users_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}, {"AAAAA": user_agent}, {"ABCD": users_agent}


@app.get("/items2/")
async def read_items(x_token: Optional[str] = Header(None)):
    return {"User-Agent": x_token}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
