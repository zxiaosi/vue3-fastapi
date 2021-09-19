#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/7 14:31
# @Author : 小四先生
# @desc :
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    print(item.dict())
    return item, '人生没有无意义的经历'


@app.put("/items/{item_id}")
async def create_item2(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    print(result)
    return result


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
