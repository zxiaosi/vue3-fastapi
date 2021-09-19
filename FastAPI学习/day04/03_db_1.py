#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/12 22:21
# @Author : 小四先生
# @desc :
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# 数据库地址
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app_1.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 多线程
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 生成工厂类，然后再有工厂类生成session会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据表的结构 用 ORM 的语言描述出来
Base = declarative_base()


class M_User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


Base.metadata.create_all(bind=engine)  # 创建数据库和表

app = FastAPI()


def get_db():
    db = SessionLocal()  # 产生一个"会话",并且用完要关闭
    try:
        yield db
    finally:
        db.close()
        print('数据库已关闭')


def get_user(db: Session, user_id: int):
    CCCC = db.query(M_User).filter(M_User.id == user_id).first()
    print('CCCC', CCCC)  # 过滤器
    return CCCC


# 新建用户(数据库)
def db_create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = M_User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # 刷新
    return db_user


# 新建用户(post请求)
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return db_create_user(db=db, user=user)


# 通过id方式读取用户
@app.get("/users/{user_id}", response_model=User)
def read_users(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
