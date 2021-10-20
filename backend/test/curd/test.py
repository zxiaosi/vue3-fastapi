#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/14 16:18
# @Author : 小四先生
# @desc :
# 依赖项
from fastapi import FastAPI, Depends

from backend.schemas import user
from backend.db.session import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()  # 绘画
    try:
        yield db
    finally:
        db.close()
        print('数据库已关闭')


# 新建用户(post请求)
@app.post("/users/", response_model=user.User)
def create_user(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        # 邮箱已注册
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.db_create_user(db=db, user=user)


# 读取用户（用户id范围）
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# 通过id方式读取用户
@app.get("/users/{user_id}", response_model=schemas.User)
def read_users(user_id: int, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# 设置用户拥有的项目(权限或作用域)
@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: SessionLocal = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


# 读取用户项目(权限或作用域)
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
