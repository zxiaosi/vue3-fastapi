#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 14:33
# @Author : 小四先生
# @desc :
from typing import Optional, List, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []
    tags1: List[str] = []
    tags2: Set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
