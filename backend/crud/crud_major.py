#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:03
# @Author : 小四先生
# @desc : 操作专业表
from typing import Union, Dict, Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Major
from schemas import MajorCreate, MajorUpdate


class CRUDMajor(CRUDBase[Major, MajorCreate, MajorUpdate]):
    def get_multi_by_department(
            self, db: Session, *, department_id: str, skip: int = 0, limit: int = 100
    ) -> List[Major]:
        """
        获取 skip-limit 的专业信息

        :param db: Session
        :param department_id: department_id 院系编号
        :param skip: 起始 (默认值0)
        :param limit: 结束 (默认值100)
        :return: 所有专业对象
        """
        return db.query(self.model).filter(Major.department_id == department_id).offset(skip).limit(limit).all()

    def create_with_department(self, db: Session, *, obj_in: MajorCreate, department_id: str) -> Major:
        """
        添加专业信息

        :param db: Session
        :param obj_in: MajorCreate 输入的专业对象
        :param department_id: 院系编号
        :return: 专业对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, department_id=department_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Major, obj_in: Union[MajorUpdate, Dict[str, Any]]
    ) -> Major:
        """
        更新对象

        :param db: Session
        :param db_obj: Major 专业对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 专业对象
        """
        if isinstance(obj_in, dict):
            department_data = obj_in
        else:
            department_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=department_data)


major = CRUDMajor(Major)
