#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/1 14:03
# @Author : zxiaosi
# @desc : 对象转字典
from sqlalchemy import inspect

from models import Resource


def obj_as_dict(obj):
    """ ORM对象转字典 """
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs} if obj else None


def list_obj_as_dict(list_obj):
    """ ORM列表对象转字典 """
    return [obj_as_dict(obj) for obj in list_obj]


def generate_tree_menu(menu_list):
    """ 生成树形菜单 """
    menu_dict = {}
    for menu in menu_list:
        menu_dict[menu["id"]] = menu
        menu_dict[menu["id"]]["children"] = []
    tree_menu = []
    for menu in menu_list:
        if menu["level"] == 2:
            continue

        if menu["pid"] == 0:
            tree_menu.append(menu)
        else:
            menu_dict[menu["pid"]]["children"].append(menu)  # type: ignore

    return tree_menu
