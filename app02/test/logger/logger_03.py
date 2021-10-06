#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/29 19:52
# @Author : 小四先生
# @desc : 调用写入文件模块 TimedRotatingFileHandler
import logging
import os
from app02.core.config import settings
from logging import handlers

# 读取配置文件
folder_name = settings.LOGGER_FOLDER
loggerName = settings.LOGGER_NAME
level = settings.LOGGER_LEVER


# 创建日志文件夹
def do_folder():
    # 获取当前文件夹
    current_path = os.path.dirname(__file__)
    print(current_path)

    # 获取当前文件夹的上一层文件
    base_path = os.path.abspath(os.path.join(current_path, ".."))
    print(base_path)

    # 拼接路径
    log_folder = base_path + os.sep + folder_name + os.sep
    print(f'日志文件夹名: {folder_name} -- {log_folder} \n')

    """如果文件夹不存在就创建"""
    os.makedirs(log_folder.strip(), exist_ok=True)

    return log_folder


# 日志功能
def my_logging():
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    # 获取 日志文件夹 路径
    log_folder = do_folder()
    log_file = log_folder + loggerName

    # 创建一个handler用于写入日志文件
    # when 时间段
    # backupCount 日志的最大个数, 超出删除最早的日志
    # delay 是否加入缓存, 不加缓存有错误(未尝试)
    fh = handlers.TimedRotatingFileHandler(filename=log_file, when='S', encoding='utf-8',
                                           backupCount=3, delay=True)

    fh.suffix = "%Y-%m-%d_%H-%M-%S.log"

    # 创建一个handler用于输出到控制台
    ch = logging.StreamHandler()

    # 定义输出格式
    date_fmt = '%Y-%m-%d %H:%M:%S'
    text_fmt = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    # text_fmt = '%(asctime)s - %(pathname)s - [line:%(lineno)d] - %(levelname)s > %(message)s'
    format_str = logging.Formatter(text_fmt, date_fmt)

    # 为文件、控制台操作符绑定格式
    fh.setFormatter(format_str)
    ch.setFormatter(format_str)

    log = logging.getLogger()
    log.setLevel(level_relations.get(level))  # 设置 日志 等级

    # 给log对象绑定文件、控制台操作符
    log.addHandler(ch)
    log.addHandler(fh)

    return log


if __name__ == '__main__':
    logger = my_logging()
    logger.debug('Debug状态')
    logger.info('输入状态')
    logger.warning('警告级别错误')
    logger.error('产生错误信息')
    logger.critical('产生严重错误')
