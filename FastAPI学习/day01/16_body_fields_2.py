#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 14:26
# @Author : 小四先生
# @desc :
from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item = Body(...,
                          example={
                              "name": "Foo",
                              "description": "A very nice Item",
                              "price": 0,
                              "tax": 3.2,
                          })):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
