#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/14 16:17
# @Author : 小四先生
# @desc :
# 通过id查询用户信息
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db.session import SessionLocal
from backend.models import user


def get_user(db: Session, user_id: int):
    return db.query(user.User).filter(user.User.id == user_id).first()


def get_db():
    db = SessionLocal()  # 绘画
    print(db)
    db.execute("SELECT 1")
    try:
        yield db
    finally:
        db.close()
        print('数据库已关闭')


def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    print("我执行了--get_users")
    print(db)
    return db.query(user.User).offset(skip).limit(limit).all()


def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    print("我执行了--read_users")
    return users


if __name__ == '__main__':
    read_users()
