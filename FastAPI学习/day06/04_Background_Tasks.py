#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 15:44
# @Author : 小四先生
# @desc :
from typing import Optional

from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI(
    # docs 中的显示设置
    title="app",
    description="This is a app",
    version="6.6.6",
    # 修改 docs 的路径
    # docs_url="/documentation",
    # redoc_url=None,
    # redoc 中的download
    openapi_url="/api/v1/openapi.json"
)


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
        email: str, background_tasks: BackgroundTasks, xxx: str = Depends(get_query)
):
    print('xxx', id(xxx))
    print(xxx)
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
