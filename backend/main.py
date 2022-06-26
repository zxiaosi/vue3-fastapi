import aioredis as aioredis
import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise

from tortoise.contrib.fastapi import register_tortoise

import router

app = FastAPI(title="Tortoise ORM FastAPI example")

app.include_router(router.router)

# https://developer.redis.com/develop/python/fastapi/#introduction
# 用后台任务redis 存数据方便, 拿数据比较麻烦
# https://aioredis.readthedocs.io/en/latest/migration/#cleaning-up
pool = aioredis.ConnectionPool.from_url("redis://:123456@localhost:6379/1", decode_responses=True)


@app.on_event("startup")
async def startup_event():
    # https://tortoise.github.io/examples/fastapi.html
    register_tortoise(
        app,
        db_url="sqlite://sql_app",
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    app.state.redis = aioredis.Redis(connection_pool=pool)


@app.on_event("shutdown")
async def read_items():
    await Tortoise.close_connections()
    await pool.disconnect()


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
