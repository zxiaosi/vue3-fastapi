#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 16:29
# @Author : 小四先生
# @desc : 操作课程表
from typing import Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Course
from schemas import CourseCreate, CourseUpdate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):
    def create(self, db: Session, *, obj_in: CourseCreate) -> Course:
        """
        添加课程信息

        :param db: Session
        :param obj_in: CourseCreate 输入的课程对象
        :return: 课程对象
        """
        db_obj = self.model(**jsonable_encoder(obj_in))  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Course, obj_in: Union[CourseUpdate, Dict[str, Any]]
    ) -> Course:
        """
        更新课程信息

        :param db: Session
        :param db_obj: Course 课程对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 课程对象
        """
        if isinstance(obj_in, dict):
            course_data = obj_in
        else:
            course_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=course_data)


course = CRUDCourse(Course)
