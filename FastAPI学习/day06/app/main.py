#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 14:49
# @Author : 小四先生
# @desc :
from fastapi import Depends, FastAPI, Header, HTTPException
from routers import users, items

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(users.router)
app.include_router(items.router,
                   # 前缀
                   prefix="/items",
                   tags=["items"],
                   # 依赖关系
                   dependencies=[Depends(get_token_header)],
                   responses={404: {"description": "Not found"}}
                   )

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
