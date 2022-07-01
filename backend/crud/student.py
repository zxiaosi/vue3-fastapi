#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:05
# @Author : zxiaosi
# @desc : 操作学生表
from typing import Union, Dict, Any

from sqlalchemy import update, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_password_hash
from crud import CRUDBase
from models import Student, Major
from schemas import StudentCreate, StudentUpdate
from utils import obj_as_dict


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    async def create(self, db: AsyncSession, obj_in: StudentCreate) -> int:
        """ 添加学生信息 """
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

    async def update(self, db: AsyncSession, id: int, obj_in: Union[StudentUpdate, Dict[str, Any]]) -> int:
        """ 更新学生信息 """
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

    # async def get_detail(self, db: AsyncSession, id: int):
    #     sql = select(self.model, Major.name.label("major_name")) \
    #         .join(Major, self.model.majorId == Major.id) \
    #         .where(self.model.id == id)
    #     result = await db.execute(sql)
    #     await db.close()  # 释放会话
    #     return result.fetchone()


student = CRUDStudent(Student)
