#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/3/9 20:44
# @Author : zxiaosi
# @desc : 权限分配
from typing import List, Union

import crud
from core import settings
from crud.admin import CRUDAdmin
from crud.teacher import CRUDTeacher
from crud.student import CRUDStudent
from utils import PermissionNotEnough


def by_scopes_get_crud(scopes: List[Union[str]]) -> Union[CRUDAdmin, CRUDTeacher, CRUDStudent]:
    """ 根据scopes(权限)分配不同的权限 """
    if 'admin' in scopes:
        return crud.admin
    elif 'teacher' in scopes:
        return crud.teacher
    elif 'student' in scopes:
        return crud.student
    else:
        raise PermissionNotEnough


def handle_oauth2_scopes():
    """ 配置 OAuth2PasswordBearer 的 scopes """
    join_dict = {}
    for item in settings.PERMISSION_DATA:
        join_dict.update(item)
    return join_dict


def generate_permission_data():
    """ 生成 permission 表数据 """
    data = []
    for item in settings.PERMISSION_DATA:
        (key, value), = item.items()  # , 一定要存在
        data.append({'name': key, 'desc': value})
    return data
