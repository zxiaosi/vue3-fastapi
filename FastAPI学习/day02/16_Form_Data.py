#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/9 16:29
# @Author : 小四先生
# @desc :
from starlette.requests import Request
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/user/")
async def users(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse('post.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
