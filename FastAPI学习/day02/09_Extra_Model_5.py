#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/9 11:16
# @Author : 小四先生
# @desc :
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
