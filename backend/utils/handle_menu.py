#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/1 14:03
# @Author : zxiaosi
# @desc : 菜单处理
from fastapi.encoders import jsonable_encoder


def generate_tree_menu(menu_obj_list):
    """ 生成树形菜单 """
    menu_list = [jsonable_encoder(menu_obj) for menu_obj in menu_obj_list]
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
