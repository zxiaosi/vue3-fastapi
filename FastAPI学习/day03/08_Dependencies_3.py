#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/10 16:31
# @Author : 小四先生
# @desc :
from typing import Optional

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
        q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
