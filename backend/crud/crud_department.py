#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/28 19:01
# @Author : 小四先生
# @desc : 操作院系表
from typing import Union, Dict, Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Department
from schemas import DepartmentCreate, DepartmentUpdate, DepartmentReturn


class CRUDDepartment(CRUDBase[DepartmentReturn, DepartmentCreate, DepartmentUpdate]):
    def get_multi_department(
            self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[DepartmentReturn]:
        """
        获取 skip-limit 的对象集

        :param db: Session
        :param skip: 起始 (默认值0)
        :param limit: 结束 (默认值100)
        :return: 查询到的对象集
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: DepartmentCreate) -> Department:
        """
        添加院系信息

        :param db: Session
        :param obj_in: DepartmentCreate 输入的院系对象
        :return: 院系对象
        """
        db_obj = Department(**jsonable_encoder(obj_in))  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Department, obj_in: Union[DepartmentUpdate, Dict[str, Any]]
    ) -> Department:
        """
        更新院系信息

        :param db: Session
        :param db_obj: Department 院系对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 院系对象
        """
        if isinstance(obj_in, dict):
            department_data = obj_in
        else:
            department_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=department_data)


department = CRUDDepartment(Department)
