#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:09
# @Author : zxiaosi
# @desc : 操作选课表
from typing import List, Any

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models import SelectCourse, Student, Course, Teacher
from schemas import SelectCourseCreate, SelectCourseUpdate


class CRUDSelectCourse(CRUDBase[SelectCourse, SelectCourseCreate, SelectCourseUpdate]):
    async def get_multi_id_name(self, db: AsyncSession, pageIndex: int = 1, pageSize: int = 10) -> List[Any]:
        """ 获取第 pageIndex 页的 pageSize 数据 """
        fields = [self.model.id, self.model.grade, self.model.course_id, self.model.student_id, self.model.teacher_id,
                  Student.name.label('student_name'), Course.name.label('course_name'),
                  Teacher.name.label('teacher_id')]
        if pageIndex == -1 and pageSize == -1:
            sql = select(*fields).order_by(desc(self.model.id))
        else:
            sql = select(*fields) \
                .join(Student, self.model.student_id == Student.id) \
                .join(Course, self.model.course_id == Course.id) \
                .join(Teacher, self.model.teacher_id == Teacher.id) \
                .offset((pageIndex - 1) * pageSize).limit(pageSize).order_by(desc(self.model.id))
        result = await db.execute(sql)
        # print(list_obj_as_dict(await db.scalars(sql)))
        await db.close()  # 释放会话
        return result.fetchall()


selectCourse = CRUDSelectCourse(SelectCourse)
