#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/29 19:47
# @Author : 小四先生
# @desc : 创建单个日志文件
import os
import logging

# 日志文件名
filename = 'test.log'


def do_file():
    # 获取当前文件夹
    current_path = os.path.dirname(__file__)
    # 获取当前文件夹的上一层文件
    base_path = os.path.dirname(current_path)

    # 拼接路径
    path = os.path.join(base_path, filename)
    print(f'{filename} -- 文件路径: {path}')

    """如果文件不存在就创建"""
    if not os.path.exists(path):
        try:
            fh = open(path, 'w')
        except IOError:
            print(f"Error: 创建 {filename} 文件成功！！！")
        else:
            print(f"创建 {filename} 文件成功！！！")
            fh.close()
    else:
        print(f"{filename} 文件已存在！！！")


def loggers():
    # 创建一个logging对象
    logger = logging.getLogger()

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(filename, mode='a', encoding='utf-8')

    # 再创建一个handler用于输出到控制台
    ch = logging.StreamHandler()

    # 定义输出格式(可以定义多个输出格式例formatter1，formatter2)
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    # 定义日志输出层级
    logger.setLevel(logging.DEBUG)

    # 定义控制台输出层级
    logger.setLevel(logging.DEBUG)

    # 为文件操作符绑定格式（可以绑定多种格式例fh.setFormatter(formatter2)）
    fh.setFormatter(formatter)

    # 为控制台操作符绑定格式（可以绑定多种格式例ch.setFormatter(formatter2)）
    ch.setFormatter(formatter)

    # 给logger对象绑定文件操作符
    logger.addHandler(fh)

    # 给logger对象绑定文件操作符
    logger.addHandler(ch)

    return logging


if __name__ == "__main__":
    log = loggers()
    log.debug('Debug状态')
    log.info('输入状态')
    log.warning('警告级别错误')
    log.error('产生错误信息')
    log.critical('产生严重错误')
