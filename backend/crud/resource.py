#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/25 22:35
# @Author : zxiaosi
# @desc : 资源表表的增删改查
from typing import Any

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Resource, UserRole, RoleResource
from schemas import UserCreate, UserUpdate


class CRUDResource(CRUDBase[Resource, UserCreate, UserUpdate]):

    def get_resource_by_user_id(self, db: Session, user_id: int) -> list[Resource] | None:
        """ 得到用户资源 """
        stmt = (
            select(self.model)
            .join(RoleResource, self.model.id == RoleResource.resource_id)
            .join(UserRole, UserRole.role_id == RoleResource.role_id)
            .where(UserRole.user_id == user_id)
            .where(self.model.is_deleted == 0)
        )
        return db.scalars(stmt).all()  # type: ignore


resource_crud = CRUDResource(Resource)
