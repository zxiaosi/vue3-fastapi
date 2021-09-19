#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/8 15:06
# @Author : 小四先生
# @desc :
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID
from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: Optional[datetime] = Body(None),
        end_datetime: Optional[datetime] = Body(None),
        repeat_at: Optional[time] = Body(None),
        process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
