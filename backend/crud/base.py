#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/29 17:47
# @Author : zxiaosi
# @desc : 封装数据库增删改查方法
from typing import Generic, TypeVar, Type, Any

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select, update, asc, desc
from sqlalchemy.orm import Session

from models import Base
from schemas import QuerySchema, OrderSchema

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """ CRUD 增 查 改 删 """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> ModelType | None:
        return db.get(self.model, id)

    def get_all(self, db: Session, query: QuerySchema | None = None, order: OrderSchema | None = None) \
            -> list[ModelType | None]:
        """ 获取所有对象 """
        stmt = select(self.model).where(self.model.is_deleted == 0)

        if query.q is not None:
            stmt = stmt.where(self.model[query.q] == query.q)

        if query.page and query.page_size:
            stmt = stmt.offset((query.page - 1) * query.page_size).limit(query.page_size)

        if order is not None:
            stmt = stmt.order_by(desc(order.field) if order.type == "desc" else asc(order.field))

        return db.scalars(stmt).all()  # type: ignore

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        """ 添加对象 """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, id: int, obj_in: UpdateSchemaType | dict[str, Any]) -> ModelType:
        """ 通过 id 更新对象 """
        if isinstance(obj_in, dict):  # 判断对象是否为字典类型(更新部分字段)
            db_obj = obj_in
        else:
            db_obj = obj_in.dict(exclude_unset=True)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj  # type: ignore

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_count(self, db: Session) -> int:
        """ 统计总数 """
        return db.query(self.model).count()
