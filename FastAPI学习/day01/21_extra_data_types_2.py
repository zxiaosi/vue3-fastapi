#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 15:10
# @Author : 小四先生
# @desc :
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    start_datetime: Optional[datetime] = Body(None)
    end_datetime: Optional[datetime] = Body(None)
    repeat_at: Optional[time] = Body(None)
    process_after: Optional[timedelta] = Body(None)
    start_process: str
    duration: str


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        item: Item
):
    item.start_process = item.start_datetime + item.process_after
    item.duration = item.end_datetime - item.start_process
    return {
        "item_id": item_id,
        "item": {**item}
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
