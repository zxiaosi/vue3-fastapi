#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 9:31
# @Author : 小四先生
# @desc :
from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: str = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
