#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/12 19:22
# @Author : 小四先生
# @desc :
from fastapi import FastAPI
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


if __name__ == '__main__':
    for i in get_db():
        c = get_user(db=i, user_id=1)
