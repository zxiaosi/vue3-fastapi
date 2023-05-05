#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/2 9:29
# @Author : zxiaosi
# @desc : 自定义日志
import logging
import os
import sys
from pprint import pformat

from loguru import logger
from loguru._defaults import LOGURU_FORMAT

from core.config import settings

"""
    如何使用 Loguru 在 FastAPI 中覆盖 Uvicorn Logger
    1. https://medium.com/1mgofficial/how-to-override-uvicorn-logger-in-fastapi-using-loguru-124133cdcd4e
    2. https://blog.csdn.net/qq_29622543/article/details/115655275
    3. https://juejin.cn/post/7063739614590140424 【使用】
"""


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def format_record(record: dict) -> str:
    """
    这里的代码是copy的，记录日志格式的
    Custom format for loguru loggers.
    Uses pformat for log any data like request/response body during debug.
    Works with logging if loguru handler it.
    Example:
    # >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
    # >>> logger.bind(payload=).debug("users payload")
    # >>> [   {   'count': 2,
    # >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
    # >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
    """

    format_string = LOGURU_FORMAT
    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=4, compact=True, width=88
        )
        format_string += "\n<level>{extra[payload]}</level>"

    format_string += "{exception}\n"
    return format_string


def init_logging():
    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn.access")
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    # 这里的操作是为了改变uvicorn默认的logger，使之采用loguru的logger
    # change handler for default uvicorn logger
    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]

    # set logs output, level and format
    logger.add(sys.stdout, level=settings.LOGGER_LEVEL, format=format_record)  # 控制台输出

    logger_name_path = os.path.join(os.getcwd() + os.sep + settings.LOGGER_DIR, settings.LOGGER_NAME)  # 日志保存路径
    logger.add(logger_name_path, enqueue=True, level=settings.LOGGER_LEVEL,
               rotation=settings.LOGGER_ROTATION, retention=settings.LOGGER_RETENTION)  # 文件输出

    # 配置loguru的日志句柄，sink代表输出的目标
    # https://loguru.readthedocs.io/en/stable/overview.html#suitable-for-scripts-and-libraries
    logger.configure(handlers=[
        {"sink": sys.stdout, "level": settings.LOGGER_LEVEL, "format": format_record},  # 控制台输出
        {"sink": logger_name_path, "level": settings.LOGGER_LEVEL, "format": format_record}  # 文件输出
    ])
    return logger


my_logger = init_logging()
