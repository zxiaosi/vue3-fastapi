#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/6 15:18
# @Author : 小四先生
# @desc : 日志模块
import logging
import os
import re
import time
from logging.handlers import TimedRotatingFileHandler

from app02.core.config import settings

# 文件夹名
folderName = settings.LOGGER_FOLDER
# 临时日志文件名
loggerName = settings.LOGGER_NAME
# 日志等级
level = settings.LOGGER_LEVER

# 日志打印等级
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


# 创建日志文件夹
def create_folder():
    # 获取当前文件夹
    current_path = os.path.dirname(__file__)

    # 获取当前文件夹的上一层文件
    base_path = os.path.abspath(os.path.join(current_path, "../../FastAPI/app02"))

    # 拼接路径
    log_dir = base_path + os.sep + folderName + os.sep
    # print(f'日志文件夹名: {folderName} -- {log_dir} \n')

    """如果文件夹不存在就创建"""
    os.makedirs(log_dir.strip(), exist_ok=True)

    return log_dir


# 继承 TimedRotatingFileHandler
class MyTimedRotatingFileHandler(TimedRotatingFileHandler):
    """重写 getFilesToDelete 方法"""

    def getFilesToDelete(self):
        dirName = create_folder()
        # 获取文件下的所有的文件(不包含 临时日志文件)
        fileNames = os.listdir(dirName)
        result = []
        for fileName in fileNames:
            result.append(os.path.join(dirName, fileName))
        if len(result) < self.backupCount:
            result = []
        else:
            result.sort()
            result = result[:len(result) - self.backupCount]
        return result


# 日志方法
def my_logger():
    # 获取 日志文件夹 路径
    log_folder = create_folder()
    log_file = log_folder + loggerName  # 拼接 日志名

    # 创建一个handler，用于写入日志文件 (每分钟生成1个，最多保留3个日志)
    # when 时间段 [ S:秒 | M:分钟 | H:小时 | D:天 | W:周(0=Monday) | midnight:午夜 ]
    # backupCount 日志的最大个数, 超出删除最早的日志
    # delay 是否加入缓存, 不加缓存有错误(未尝试)
    fh = MyTimedRotatingFileHandler(filename=log_file, when='S', backupCount=3, encoding='utf-8', delay=True)
    fh.suffix = "%Y-%m-%d_%H-%M-%S.log"  # 日志文件的后缀名
    fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$")  # 匹配日志文件名

    # 修改日志文件名 [ log.2021-10-06_23-22-35.log --> 2021-10-06_23-22-35.log ]
    def namer(filename):
        return filename.replace(loggerName + ".", "")

    fh.namer = namer

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()

    # 单独设置日志等级
    # fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

    # 定义输出格式
    datefmt = '%Y-%m-%d %H:%M:%S'
    format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s \n'
    # format = '%(asctime)s - %(pathname)s - [line:%(lineno)d] - %(levelname)s > %(message)s \n'
    format_str = logging.Formatter(format, datefmt)

    # 为文件、控制台操作符绑定格式
    fh.setFormatter(format_str)
    ch.setFormatter(format_str)

    # 创建一个logging对象
    log = logging.getLogger()
    log.setLevel(LEVELS.get(level))  # 定义日志输出层级

    # 给log添加handler
    log.addHandler(fh)
    log.addHandler(ch)

    return log


# 初始化日志
logger = my_logger()

# logger.debug('Debug状态')
# time.sleep(2)
# logger.info('输入状态')
# time.sleep(2)
# logger.warning('警告级别错误')
# time.sleep(2)
# logger.error('产生错误信息')
# time.sleep(2)
# logger.critical('产生严重错误')
# time.sleep(2)
