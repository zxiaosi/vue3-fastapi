#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 15:57
# @Author : 小四先生
# @desc :
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
