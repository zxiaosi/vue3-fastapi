#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 15:39
# @Author : 小四先生
# @desc :
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(response.headers)
    return response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
