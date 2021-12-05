#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/18 10:09
# @Author : 小四先生
# @desc : 操作选课表
from typing import Union, Dict, Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import SelectCourse, Teacher, Student, Course
from schemas import SelectCourseReturn, SelectCourseCreate, SelectCourseUpdate


class CRUDSelectCourse(CRUDBase[SelectCourse, SelectCourseCreate, SelectCourseUpdate]):
    def get_multi_select_course(
            self, db: Session, *, skip: int = 0, limit: int = 100, id: Any = None
    ) -> List[SelectCourseReturn]:
        """
        获取 skip-limit 的选课信息

        :param db: Session
        :param skip: 起始 (默认值0)
        :param limit: 结束 (默认值100)
        :param id: 选课id (可选参数)
        :return: 所有选课对象
        """

        custom_filter = [
            self.model.id, self.model.grade,
            self.model.student_id, self.model.teacher_id, self.model.course_id,
            Student.name.label('student_name'), Teacher.name.label('teacher_name'), Course.name.label('course_name')
        ]

        if id:
            return db.query(*custom_filter).filter(self.model.id == id).first()
        else:
            return db.query(*custom_filter).join(Student, Teacher, Course).offset(skip).limit(limit).all()

    def create_select_course(self, db: Session, *, obj_in: SelectCourseCreate) -> SelectCourse:
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
            self, db: Session, *, db_obj: SelectCourse, obj_in: Union[SelectCourseUpdate, Dict[str, Any]]
    ) -> SelectCourse:
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


selectCourse = CRUDSelectCourse(SelectCourse)
