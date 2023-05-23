#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/25 22:35
# @Author : zxiaosi
# @desc : 资源表表的增删改查
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Resource, UserRole, RoleResource, Role
from schemas import UserCreate, UserUpdate, PageSchema


class CRUDResource(CRUDBase[Resource, UserCreate, UserUpdate]):

    def get_all(self, db: Session, page: PageSchema, name: str = None, *args) -> list[Role | None]:
        stmt = select(self.model)
        if name is not None:
            stmt.where(self.model.name == name)

        stmt = stmt.offset((page.page - 1) * page.page_size).limit(page.page_size)
        return db.scalars(stmt).all()  # type: ignore

    def get_resource_by_role_id(self, db: Session, role_id: int) -> list[Resource] | None:
        """ 根据角色id得到资源 """
        stmt = (
            select(self.model)
            .join(RoleResource, self.model.id == RoleResource.resource_id)
            .where(RoleResource.role_id == role_id)
            .where(self.model.is_deleted == 0)
        )
        return db.scalars(stmt).all()  # type: ignore

    def get_resource_by_role_code(self, db: Session, role_code: str) -> list[Resource] | None:
        """ 根据角色code得到资源 """
        stmt = (
            select(self.model)
            .join(RoleResource, self.model.id == RoleResource.resource_id)
            .join(Role, Role.id == RoleResource.role_id)
            .where(Role.code == role_code)
            .where(self.model.is_deleted == 0)
        )
        return db.scalars(stmt).all()  # type: ignore

    def get_resource_by_user_id(self, db: Session, user_id: int) -> list[Resource] | None:
        """ 根据用户id得到资源 """
        stmt = (
            select(self.model)
            .join(RoleResource, self.model.id == RoleResource.resource_id)
            .join(UserRole, UserRole.role_id == RoleResource.role_id)
            .where(UserRole.user_id == user_id)
            .where(self.model.is_deleted == 0)
        )
        return db.scalars(stmt).all()  # type: ignore

    def get_resource_by_url(self, db: Session, url: str) -> Resource | None:
        """ 得到资源 """
        stmt = (
            select(self.model)
            .where(self.model.request_url == url)
            .where(self.model.is_deleted == 0)
        )
        return db.scalar(stmt)


resource_crud = CRUDResource(Resource)
