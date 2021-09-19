#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/7 11:05
# @Author : 小四先生
# @desc :
from fastapi import FastAPI
from enum import Enum


class Name(str, Enum):
    Allan = '张三'
    Jon = '李四'
    Bob = '王五'


app = FastAPI()


@app.get("/{who}")
async def get_day(who: Name):
    if who == Name.Allan:
        return {"who": who, "message": "张三是德国人"}

    if who.value == "李四":
        return {"who": who, "message": "李四是英国人"}

    return {"who": who, "message": "王五是法国人"}


# 路径转换器
@app.get("/file/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/")
async def main():
    return {"mesaage": "Hello, FastAPI"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
