#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:05
# @Author : 小四先生
# @desc : 操作学生表
from datetime import datetime
from typing import Union, Dict, Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.security import get_password_hash
from crud.base import CRUDBase
from models import Student, Major
from schemas import StudentReturn, StudentCreate, StudentUpdate


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def create(self, db: Session, *, obj_in: StudentCreate) -> Student:
        """
        添加学生信息

        :param db: Session
        :param obj_in: StudentCreate 输入的学生对象
        :return: 学生对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            id=obj_in_data['id'],
            name=obj_in_data['name'],
            sex=obj_in_data['sex'],
            birthday=datetime.strptime(obj_in_data['birthday'], "%Y-%m-%d").date(),
            hashed_password=get_password_hash(obj_in_data['password']),
            major_id=obj_in_data['major_id']
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Student, obj_in: Union[StudentUpdate, Dict[str, Any]]
    ) -> Student:
        """
        更新学生信息

        :param db: Session
        :param db_obj: MStudent 学生对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 学生对象
        """
        if isinstance(obj_in, dict):
            student_data = obj_in
        else:
            student_data = obj_in.dict(exclude_unset=True)
        if student_data["password"]:
            hashed_password = get_password_hash(student_data["password"])
            del student_data["password"]
            student_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=student_data)


student = CRUDStudent(Student)
