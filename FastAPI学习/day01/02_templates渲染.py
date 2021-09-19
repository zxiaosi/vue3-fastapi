#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/8/25 15:43
# @Author : 小四先生
# @desc :
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'hello': 'HI...'})


@app.get("/{items_id}/")
async def read_item(request: Request, items_id):
    return templates.TemplateResponse("index.html", {"request": request, "items_id": items_id})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
