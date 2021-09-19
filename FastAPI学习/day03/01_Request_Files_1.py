#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/10 15:39
# @Author : 小四先生
# @desc :
from fastapi import FastAPI, File, UploadFile
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/create_file/")
async def create_file(file: bytes = File(...), fileb: UploadFile = File(...)):
    return {"file_size": len(file),
            "fileb_content_type": fileb.content_type}


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('post.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
