#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/14 17:01
# @Author : 小四先生
# @desc : 用户表--增删改查方法
from utils.logger import logger
from typing import Any, Dict, Union, Optional

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models import User
from schemas import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """
        添加用户

        :param db: Session
        :param obj_in: UserCreate 输入的用户对象
        :return: 用户对象
        """
        db_obj = User(
            full_name=obj_in.full_name,
            hashed_password=get_password_hash(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        """
        更新对象

        :param db: Session
        :param db_obj: User 用户对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 用户对象
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    # 通过名字得到用户
    def get_by_name(self, db: Session, *, name: str) -> Optional[User]:
        return db.query(User).filter(User.full_name == name).first()

    # 验证用户
    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user = self.get_by_name(db, name=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    # 验证用户是否登录
    def is_active(self, user: User) -> bool:
        return user.is_active


user = CRUDUser(User)
