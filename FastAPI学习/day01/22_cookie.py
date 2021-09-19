#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 15:18
# @Author : 小四先生
# @desc :
from typing import Optional
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
