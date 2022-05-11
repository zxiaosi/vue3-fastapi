#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:09
# @Author : zxiaosi
# @desc : 操作选课表
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models import Elective, Taught, Student, Teacher, Course
from schemas import ElectiveCreate, ElectiveUpdate
from utils import obj_as_dict, list_obj_as_dict


class CRUDElective(CRUDBase[Elective, ElectiveCreate, ElectiveUpdate]):
    async def get_course(self, db: AsyncSession, id: Any) -> Any:
        """ 通过 id 获取对象 """
        fields = [self.model.grade, Course.name.label('course_name'), Teacher.name.label('teacher_name'),
                  self.model.update_time]
        sql = select(*fields).where(self.model.student_id == int(id)) \
            .join(Course, self.model.course_id == Course.id) \
            .join(Taught, self.model.course_id == Taught.course_id, isouter=True) \
            .join(Teacher, Taught.teacher_id == Teacher.id, isouter=True)
        print(id, sql)
        result = await db.execute(sql)
        # print(list_obj_as_dict(result.all()))
        await db.close()  # 释放会话
        return result.fetchall()

    async def is_exist(self, db: AsyncSession, student_id: int, course_id: int) -> int:
        """ 判断数据是否已经存在 """
        sql1 = select(self.model) \
            .where(self.model.student_id == student_id) \
            .where(self.model.course_id == course_id)
        result = await db.scalar(sql1)
        return result

    async def create(self, db: AsyncSession, obj_in: Elective) -> int:
        """ 添加对象 """
        return await super().create(db, obj_in=obj_in)  # noqa


elective = CRUDElective(Elective)
