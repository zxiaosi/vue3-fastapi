#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/11 11:05
# @Author : zxiaosi
# @desc : 对象转字典
from sqlalchemy import inspect


def obj_as_dict(obj):
    """ ORM对象转字典 """
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs} if obj else None


def list_obj_as_dict(list_obj):
    """ ORM列表对象转字典 """
    return [obj_as_dict(obj) for obj in list_obj]
