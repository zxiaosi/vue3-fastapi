#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/6 15:18
# @Author : 小四先生
# @desc : 日志模块
import os
import re
import threading

import logging
import time

from logging.handlers import TimedRotatingFileHandler


# 创建日志文件夹
def create_folder(folder_name):
    """
    创建日志文件夹

    :param folder_name: 文件名
    :return: 日志路径
    """
    # 获取当前文件夹
    current_path = os.path.dirname(__file__)

    # 获取当前文件夹的上一层文件
    base_path = os.path.abspath(os.path.join(current_path, ".."))

    # 拼接路径
    log_dir = base_path + os.sep + folder_name + os.sep
    # print(f'日志文件夹名: {folder_name} -- {log_dir} \n')

    """如果文件夹不存在就创建"""
    os.makedirs(log_dir.strip(), exist_ok=True)

    return log_dir


# 继承 TimedRotatingFileHandler
class MyTimedRotatingFileHandler(TimedRotatingFileHandler):
    """重写 getFilesToDelete 方法"""

    def getFilesToDelete(self):
        dirName = os.path.abspath(os.path.join(self.baseFilename, ".."))
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


# log日志
class MyLogger:
    """
    封装 log日志

    :param folderName: 文件夹名
    :param logname: 临时日志文件名
    :param level: 日志级别
    :param datefmt: 时间格式化
    :param fmt: 格式化
    :param console: 是否输出到控制台
    :param file: 保存的日志文件名
    :param when: 日志按时间切分(默认天)
    :param backCount: 备份文件最大个数,超过删除
    :return: 日志对象
    """
    # 使用线程锁保证单例模式线程安全
    _instance_lock = threading.Lock()

    def start(self, *args, **kwargs):
        # 接收参数
        self.folderName = (kwargs["folderName"] if kwargs.get("folderName") else "logs")  # 日志文件夹名
        self.logname = (kwargs["tempName"] if kwargs.get("tempName") else "log")  # 临时日志文件名
        self.level = (kwargs["level"] if kwargs.get("level") else "debug")  # 日志级别
        self.datefmt = (kwargs["datefmt"] if kwargs.get("datefmt") else None)  # 时间格式化
        self.fmt = (kwargs["format"] if kwargs.get("format")
                    else "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  # 格式化
        self.console = (kwargs["console"] if kwargs.get("console") else True)  # 是否输出到控制台
        self.file = (kwargs["file"] if kwargs.get("file")
                     else (create_folder(self.folderName) + self.logname))  # 保存的文件名
        self.when = (kwargs["when"] if kwargs.get("when") else "D")  # 日志按时间切分(默认天)
        self.backCount = (kwargs["backCount"] if kwargs.get("backCount") else 30)  # 备份文件最大个数,超过删除

        # 设置loggin参数
        self.level_relations = {  # 日志级别
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        self.logger = logging.getLogger(__name__)
        self.format = logging.Formatter(self.fmt, self.datefmt)

        if not self.level_relations.get(self.level):
            self.level = "debug"
        self.logger.setLevel(self.level_relations[self.level])
        if self.console:
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(self.format)
            self.logger.addHandler(streamHandler)
        if self.file:  # log存档,按时间切割存档
            timeHandler = MyTimedRotatingFileHandler(
                filename=self.file,
                when=self.when,
                backupCount=self.backCount,
                encoding="utf-8"
            )
            timeHandler.suffix = "%Y-%m-%d_%H-%M-%S.log"  # 日志文件的后缀名
            timeHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$")  # 匹配日志文件名

            # 修改日志文件名 [ log.2021-10-06_23-22-35.log --> 2021-10-06_23-22-35.log ]
            def namer(filename):
                return filename.replace(self.logname + ".", "")

            timeHandler.namer = namer
            timeHandler.setFormatter(self.format)
            self.logger.addHandler(timeHandler)

    # 单例模式实现
    def __new__(cls, *args, **kwargs):
        # 单例模式，单个进程内永远只有一个MyLogger对象
        # 实例化先走__new__再走__init__
        if not hasattr(MyLogger, "_instance"):  # 先检查该类有没有 _instance属性
            with MyLogger._instance_lock:  # 线程安全所 同一时间只有一个线程访问这里
                if not hasattr(MyLogger, "_instance"):  # 防止等待过程已经生成新对象
                    MyLogger._instance = object.__new__(cls)  # 走__new__实例化对象并赋值给_instance
                    MyLogger._instance.start(*args, **kwargs)  # 手动调用start

                time.sleep(1)  # 防止刚实例化就写入有可能导致数据丢失,等待一下
                return MyLogger._instance.logger


if __name__ == '__main__':
    s = MyLogger(folderName="logger", when="S", backCount=3)
    s.warning("warning")
    time.sleep(2)
    s.info("info")
    time.sleep(2)
    s.error("error")
    time.sleep(2)
    s.critical("critical")
    time.sleep(2)
    s.debug("debug")
    time.sleep(2)
