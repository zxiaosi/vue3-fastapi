#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 14:54
# @Author : 小四先生
# @desc :

from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


# 纯列表体
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


# 任意字典
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
