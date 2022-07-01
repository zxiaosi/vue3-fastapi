#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/3/4 15:48
# @Author : zxiaosi
# @desc : 创建文件夹
import os


# 请不要随意移动该文件,创建文件夹是根据当前文件位置来创建
def create_dir(file_name: str) -> str:
    """ 创建文件夹 """
    current_path = os.path.dirname(__file__)  # 获取当前文件夹

    base_path = os.path.abspath(os.path.join(current_path, ".."))  # 获取当前文件夹的上一层文件

    path = base_path + os.sep + file_name + os.sep  # 拼接日志文件夹的路径

    os.makedirs(path, exist_ok=True)  # 如果文件夹不存在就创建

    return path
