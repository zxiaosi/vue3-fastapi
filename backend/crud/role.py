#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/4/23 17:11
# @Author : zxiaosi
# @desc : 角色表的增删改查
from sqlalchemy import select
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Role, UserRole
from schemas import RoleIn, PageSchema


class CRUDUserRole(CRUDBase[Role, RoleIn, RoleIn]):

    def get_all(self, db: Session, page: PageSchema, name: str = None, *args) -> list[Role | None]:
        stmt = select(self.model)
        if name is not None:
            stmt.where(self.model.name == name)

        return super().get_all(db=db, page=page, sql=stmt)

    def get_role_by_user_id(self, db: Session, user_id: int) -> Role | None:
        """ 通过用户id获取角色 """
        stmt = (
            select(Role)
            .join(UserRole, UserRole.role_id == Role.id)
            .where(UserRole.user_id == user_id)
            .where(Role.is_deleted == 0)
        )
        return db.scalar(stmt)

    def get_role_by_code(self, db: Session, code: str) -> Role | None:
        """ 通过角色名获取角色 """
        stmt = select(self.model).where(self.model.code == code).where(Role.is_deleted == 0)
        return db.scalar(stmt)


role_crud = CRUDUserRole(Role)
