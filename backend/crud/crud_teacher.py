#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/15 19:53
# @Author : 小四先生
# @desc : 操作教师表
from datetime import datetime
from typing import Union, Dict, Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.security import get_password_hash
from crud.base import CRUDBase
from models import Teacher, Department
from schemas import TeacherReturn, TeacherCreate, TeacherUpdate


class CRUDTeacher(CRUDBase[Teacher, TeacherCreate, TeacherUpdate]):
    def get_multi_teacher(
            self, db: Session, *, skip: int = 0, limit: int = 100, id: Any = None
    ) -> Union[TeacherReturn, List[TeacherReturn]]:
        """
        获取 skip-limit 的教师信息

        :param db: Session
        :param skip: 起始 (默认值0)
        :param limit: 结束 (默认值100)
        :param id: 教师id (可选参数)
        :return: 所有教师对象
        """
        custom_filter = [
            self.model.id, self.model.name, self.model.sex, self.model.birthday, self.model.education,
            self.model.title, self.model.department_id, Department.name.label('department_name')
        ]

        if id:
            return db.query(*custom_filter).filter(self.model.id == id).first()
        else:
            return db.query(*custom_filter).join(Department).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: TeacherCreate) -> Teacher:
        """
        添加教师信息

        :param db: Session
        :param obj_in: TeacherCreate 输入的教师对象
        :return: 教师对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            id=obj_in_data['id'],
            name=obj_in_data['name'],
            sex=obj_in_data['sex'],
            birthday=datetime.strptime(obj_in_data['birthday'], "%Y-%m-%d").date(),
            hashed_password=get_password_hash(obj_in_data['password']),
            education=obj_in_data['education'],
            title=obj_in_data['title'],
            department_id=obj_in_data['department_id']
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Teacher, obj_in: Union[TeacherUpdate, Dict[str, Any]]
    ) -> Teacher:
        """
        更新教师信息

        :param db: Session
        :param db_obj: MTeacher 教师对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 教师对象
        """
        if isinstance(obj_in, dict):
            teacher_data = obj_in
        else:
            teacher_data = obj_in.dict(exclude_unset=True)
        if teacher_data["password"]:
            hashed_password = get_password_hash(teacher_data["password"])
            del teacher_data["password"]
            teacher_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=teacher_data)


teacher = CRUDTeacher(Teacher)
