#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/8/25 16:43
# @Author : 小四先生
# @desc :
from typing import List
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.post("/files/")
async def files(
        request: Request,
        files_list: List[bytes] = File(...),
        files_name: List[UploadFile] = File(...)
):
    return templates.TemplateResponse('index.html',
                                      {
                                          'request': request,
                                          'file_sizes': [len(file) for file in files_list],
                                          'filesnames': [file.filename for file in files_name]
                                      })


@app.post("/create_file/")
async def create_file(
        request: Request,
        file: bytes = File(...),
        fileb: UploadFile = File(...),
        notes: str = File(...)
):
    return templates.TemplateResponse('post.html',
                                      {
                                          'request': request,
                                          'file_size': len(file),
                                          'notes': notes,
                                          'fileb_content_type': fileb.content_type,
                                      })


@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("post.html", {"request": request})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
