#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/15 19:53
# @Author : zxiaosi
# @desc : 操作教师表
from typing import Union, Dict, Any

from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_password_hash
from crud.base import CRUDBase
from models import Teacher
from schemas import TeacherCreate, TeacherUpdate


class CRUDTeacher(CRUDBase[Teacher, TeacherCreate, TeacherUpdate]):
    async def create(self, db: AsyncSession, obj_in: TeacherCreate) -> int:
        """ 添加教师信息 """
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

    async def update(self, db: AsyncSession, id: int, obj_in: Union[TeacherUpdate, Dict[str, Any]]) -> int:
        """ 更新教师信息 """
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


teacher = CRUDTeacher(Teacher)
