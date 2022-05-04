#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:05
# @Author : zxiaosi
# @desc : 操作管理员表
from typing import Union, Dict, Any
from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_password_hash
from crud import CRUDBase
from models import Admin
from schemas import AdminCreate, AdminUpdate


class CRUDAdmin(CRUDBase[Admin, AdminCreate, AdminUpdate]):
    async def create(self, db: AsyncSession, obj_in: AdminCreate) -> int:
        """ 添加管理员信息 """
        setattr(obj_in, 'id', int(obj_in.id))  # postgresql 字段类型限制
        obj_in_data = {}
        for k, v in obj_in.dict().items():  # 排除空值
            if v:
                if k == 'password':
                    obj_in_data['hashed_password'] = get_password_hash(obj_in.password)
                else:
                    obj_in_data[k] = v
        sql = insert(self.model).values(obj_in_data)
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount

    async def update(self, db: AsyncSession, id: int, obj_in: Union[AdminUpdate, Dict[str, Any]]) -> int:
        """ 更新管理员信息 """
        if isinstance(obj_in, dict):  # 判断对象是否为字典类型(更新部分字段)
            teacher_data = obj_in
        else:
            teacher_data = obj_in.dict(exclude_unset=True)
        obj_data = {}
        for k, v in teacher_data.items():  # 排除空值
            if v:
                if k == 'password':
                    obj_data['hashed_password'] = get_password_hash(obj_in.password)
                else:
                    obj_data[k] = v
        sql = update(self.model).where(self.model.id == id).values(obj_data)
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount


admin = CRUDAdmin(Admin)
