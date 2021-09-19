#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/8/25 15:43
# @Author : 小四先生
# @desc :
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {'message': 'HelloWorld, FastAPI'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
