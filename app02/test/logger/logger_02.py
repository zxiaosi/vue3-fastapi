#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/30 17:13
# @Author : 小四先生
# @desc : 调用写入文件模块 FileHandler
import logging
import os.path
import time

from app02.core.config import settings

# 读取配置文件
folder_name = settings.LOGGER_FOLDER


def my_logging():
    # 第一步，创建一个logger
    log = logging.getLogger()
    # Log等级总开关
    log.setLevel(logging.DEBUG)

    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    print(f"当前时间--{rq}")
    log_path = os.path.dirname(os.getcwd()) + os.sep + folder_name + os.sep
    print(f"当前路径--{log_path}")

    """如果文件夹不存在就创建"""
    os.makedirs(log_path.strip(), exist_ok=True)

    # 拼接日志名
    logfile = log_path + rq + '.log'
    fh = logging.FileHandler(filename=logfile, mode='w', encoding='utf-8')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第四步，将logger添加到handler里面
    log.addHandler(fh)
    log.addHandler(ch)

    return log


if __name__ == '__main__':
    logger = my_logging()
    logger.debug('Debug状态')
    logger.info('输入状态')
    logger.warning('警告级别错误')
    logger.error('产生错误信息')
    logger.critical('产生严重错误')
