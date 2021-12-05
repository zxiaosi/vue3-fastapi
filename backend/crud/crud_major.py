#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/1 21:03
# @Author : 小四先生
# @desc : 操作专业表
from typing import Union, Dict, Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Major, Department
from schemas import MajorReturn, MajorCreate, MajorUpdate


class CRUDMajor(CRUDBase[Major, MajorCreate, MajorUpdate]):
    def get_multi_major(
            self, db: Session, *, skip: int = 0, limit: int = 100, id: Any = None
    ) -> Union[MajorReturn, List[MajorReturn]]:
        """
        获取 skip-limit 的专业信息

        :param db: Session
        :param skip: 起始 (默认值0)
        :param limit: 结束 (默认值100)
        :param id: 专业id (可选参数)
        :return: 所有专业对象
        """
        custom_filter = [
            self.model.id, self.model.name, self.model.assistant, self.model.phone,
            self.model.department_id, Department.name.label('department_name')
        ]

        if id:
            return db.query(*custom_filter).filter(self.model.id == id).first()
        else:
            return db.query(*custom_filter).join(Department).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: MajorCreate) -> Major:
        """
        添加专业信息

        :param db: Session
        :param obj_in: MajorCreate 输入的专业对象
        :return: 专业对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Major, obj_in: Union[MajorUpdate, Dict[str, Any]]
    ) -> Major:
        """
        更新专业信息

        :param db: Session
        :param db_obj: Major 专业对象
        :param obj_in: UpdateSchemaType schemas类型
        :param obj_in: Dict[str, Any] 字典数据
        :return: 专业对象
        """
        if isinstance(obj_in, dict):
            major_data = obj_in
        else:
            major_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=major_data)


major = CRUDMajor(Major)
