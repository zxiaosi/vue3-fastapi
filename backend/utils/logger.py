#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/8 10:44
# @Author : zxiaosi
# @desc : 日志
import os
from loguru import logger

from core import settings


# 创建日志文件夹
def logger_dir() -> str:
    """ 创建日志文件夹 """

    current_path = os.path.dirname(__file__)  # 获取当前文件夹

    base_path = os.path.abspath(os.path.join(current_path, ".."))  # 获取当前文件夹的上一层文件

    log_path = base_path + os.sep + settings.LOGGER_FOLDER + os.sep  # 拼接日志文件夹的路径

    os.makedirs(log_path, exist_ok=True)  # 如果文件夹不存在就创建

    return log_path


# 创建日志文件名
def logger_file() -> str:
    """ 创建日志文件名 """
    log_path = logger_dir()

    """ 保留日志文件夹下最大个数(本地调试用) 
    本地调式需要多次重启, 日志轮转片不会生效 """
    file_list = os.listdir(log_path)
    if len(file_list) > 4:
        os.remove(os.path.join(log_path, file_list[0]))

    # 日志输出路径
    return os.path.join(log_path, settings.LOGGER_NAME)


# 详见: https://loguru.readthedocs.io/en/stable/overview.html#features
logger.add(
    logger_file(),
    encoding=settings.GLOBAL_ENCODING,
    level=settings.LOGGER_LEVEL,
    rotation=settings.LOGGER_ROTATION,
    retention=settings.LOGGER_RETENTION,
    enqueue=True
)

# 导出
# __all__ = ["logger"]
