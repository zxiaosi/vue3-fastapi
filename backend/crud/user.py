#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 18:41
# @Author : zxiaosi
# @desc : 用户表的增删改查
from typing import Any

from sqlalchemy import select, insert, Select
from sqlalchemy.orm import Session

from core.security import get_password_hash
from crud.base import CRUDBase
from models import User
from schemas import UserCreate, UserUpdate, PageSchema


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_all(self, db: Session, page: PageSchema, name: str = None, *args) -> list[User | None]:
        stmt = select(self.model)
        if name is not None:
            stmt.where(self.model.name == name)

        return super().get_all(db=db, page=page, sql=stmt)

    def create(self, db: Session, obj_in: UserCreate) -> User:
        """ 创建用户 """
        setattr(obj_in, 'password', get_password_hash(obj_in.password))
        return super().create(db, obj_in=obj_in)

    def get_user_by_name(self, db: Session, name: Any) -> User | None:
        stmt = select(self.model).where(self.model.name == name).where(self.model.is_deleted == 0)
        return db.scalars(stmt).one()


user_crud = CRUDUser(User)
