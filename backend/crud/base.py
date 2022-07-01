#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/14 17:00
# @Author : zxiaosi
# @desc : 封装数据库增删改查方法
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from pydantic import BaseModel
from sqlalchemy import func, distinct, select, insert, update, desc, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core import verify_password
from models import Base
from utils import obj_as_dict, list_obj_as_dict

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


# db.scalar(sql) 返回的是标量(原始数据) <models.department.Department object at 0x000002F2C2D22110>
# db.execute(sql) 返回的是元组 (<models.department.Department object at 0x000002F2C2D22110>)
# db.scalars(sql).all()  [<models...>, <models...>, <models...>]
# db.execute(sql).fetchall()  [(<models...>,), (<models...>,), (<models...>,)]
class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """ CRUD 增 查 改 删 """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        """ 通过 id 获取对象 """
        sql = select(self.model).where(self.model.id == id)
        result = await db.scalar(sql)
        # print(obj_as_dict(await db.scalar(sql)))
        await db.close()  # 释放会话
        return result

    async def get_multi(self, db: AsyncSession, pageIndex: int = 1, pageSize: int = 10) -> List[ModelType]:
        """ 获取第 pageIndex 页的 pageSize 数据 """
        if pageIndex == -1 and pageSize == -1:
            sql = select(self.model).order_by(desc(self.model.id))
        else:
            sql = select(self.model).offset((pageIndex - 1) * pageSize).limit(pageSize).order_by(desc(self.model.id))
        result = await db.scalars(sql)
        # print(list_obj_as_dict(await db.scalars(sql)))
        await db.close()  # 释放会话
        return result.all()

    async def get_number(self, db: AsyncSession) -> int:
        """ 获取表的总条数 """
        sql = select(func.count(distinct(self.model.id)))
        result = await db.scalar(sql)
        await db.close()  # 释放会话
        return result

    async def create(self, db: AsyncSession, obj_in: CreateSchemaType) -> int:
        """ 添加对象 """
        if self.model.__tablename__ not in ['taught', 'elective']:
            setattr(obj_in, 'id', int(obj_in.id))  # postgresql 字段类型限制
        sql = insert(self.model).values(obj_in.dict())
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount

    async def update(self, db: AsyncSession, id: int, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> int:
        """ 通过 id 更新对象 """
        if isinstance(obj_in, dict):  # 判断对象是否为字典类型(更新部分字段)
            obj_data = obj_in
        else:
            obj_data = obj_in.dict()
        sql = update(self.model).where(self.model.id == id).values(obj_data)
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount

    async def remove(self, db: AsyncSession, id: int) -> int:
        """ 通过 id 删除对象 """
        sql = delete(self.model).where(self.model.id == id)
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount

    async def remove_multi(self, db: AsyncSession, id_list: list):
        """ 同时删除多个对象 """
        id_list = [int(i) for i in id_list]  # postgresql 字段类型限制
        sql = delete(self.model).where(self.model.id.in_(id_list))
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount

    async def get_multi_relation(self, db: AsyncSession):
        """ 获取关系字段 """
        sql = select(self.model.id, self.model.name).order_by(desc(self.model.id)).distinct()
        result = await db.execute(sql)
        await db.close()
        return result.fetchall()

    async def get_by_name(self, db: AsyncSession, name: str) -> Optional[ModelType]:
        """ 通过名字得到用户 """
        sql = select(self.model).where(self.model.name == name)
        result = await db.scalar(sql)
        await db.close()  # 释放会话
        return result

    async def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[ModelType]:
        """ 验证用户 """
        user = await self.get_by_name(db, name=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def sort(self, db: AsyncSession, name: str, pageIndex: int = 1, pageSize: int = 10) -> List[ModelType]:
        """ 验证用户 """
        filed_name = self.model.__table__.c[name]
        if pageIndex == -1 and pageSize == -1:
            sql = select(self.model).order_by(desc(filed_name))
        else:
            sql = select(self.model).offset((pageIndex - 1) * pageSize).limit(pageSize).order_by(desc(filed_name))
        result = await db.scalars(sql)
        # print(list_obj_as_dict(await db.scalars(sql)))
        await db.close()  # 释放会话
        return result.all()
