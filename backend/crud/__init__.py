#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/14 16:59
# @Author : 小四先生
# @desc : 数据库的增删改查操作
""" 抛出操作表数据文件中的类 """
from .crud_user import user
from .crud_department import department
from .crud_major import major
from .crud_teacher import teacher

# 对于一个新的基本CRUD操作集，您可以直接执行

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
