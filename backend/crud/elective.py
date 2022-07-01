#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:09
# @Author : zxiaosi
# @desc : 操作选课表
from typing import Any, Union

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models import Elective, Taught, Student, Teacher, Course
from schemas import ElectiveCreate, ElectiveUpdate
from utils import obj_as_dict, list_obj_as_dict


class CRUDElective(CRUDBase[Elective, ElectiveCreate, ElectiveUpdate]):
    async def get_course(self, db: AsyncSession, id: Any) -> Any:
        """ 得到课程详情 """
        fields = [self.model.courseId, Course.name.label('courseName'),
                  Teacher.id.label('teacherId'), Teacher.name.label('teacherName'),
                  self.model.grade, self.model.create_time]
        sql = select(*fields).where(self.model.studentId == int(id)) \
            .join(Course, self.model.courseId == Course.id) \
            .join(Taught, self.model.courseId == Taught.courseId, isouter=True) \
            .join(Teacher, Taught.teacherId == Teacher.id, isouter=True)
        print(id, sql)
        result = await db.execute(sql)
        # print(list_obj_as_dict(result.all()))
        await db.close()  # 释放会话
        return result.fetchall()

    async def is_exist(self, db: AsyncSession, studentId: int, courseId: int) -> int:
        """ 判断数据是否已经存在 """
        sql1 = select(self.model) \
            .where(self.model.studentId == studentId) \
            .where(self.model.courseId == courseId)
        result = await db.scalar(sql1)
        return result

    async def create(self, db: AsyncSession, obj_in: Union[Elective]) -> int:
        """ 添加对象 """
        if isinstance(obj_in, dict):  # 判断对象是否为字典类型(更新部分字段)
            obj_data = obj_in
        else:
            obj_data = obj_in.dict()
        sql = insert(self.model).values(obj_data)
        result = await db.execute(sql)
        await db.commit()
        return result.rowcount


elective = CRUDElective(Elective)
