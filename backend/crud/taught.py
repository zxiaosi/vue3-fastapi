#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/5/10 21:00
# @Author : zxiaosi
# @desc : 操作讲授表
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud import CRUDBase
from models import Taught, Course, Student, Elective
from schemas import TaughtCreate, TaughtUpdate


class CRUDTaught(CRUDBase[Taught, TaughtCreate, TaughtUpdate]):
    async def get_course(self, db: AsyncSession, id: Any) -> Any:
        """ 得到课程详情 """
        fields = [self.model.courseId, Course.name.label('courseName'),
                  Elective.studentId, Student.name.label('studentName'),
                  Elective.id, Elective.grade, Elective.update_time]
        sql = select(*fields).where(self.model.teacherId == int(id)) \
            .join(Elective, self.model.courseId == Elective.courseId, isouter=True) \
            .join(Course, self.model.courseId == Course.id) \
            .join(Student, Elective.studentId == Student.id)
        result = await db.execute(sql)
        # print(list_obj_as_dict(result.all()))
        await db.close()  # 释放会话
        return result.fetchall()


taught = CRUDTaught(Taught)
