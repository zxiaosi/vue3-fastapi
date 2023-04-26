#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/4/26 15:18
# @Author : zxiaosi
# @desc : 时间处理工具类
import datetime
import time


def get_current_time():
    """ 获取当前时间(Asia/Shanghai) """

    timestamp = time.time()  # 获取当前时间戳

    offset = datetime.timezone(datetime.timedelta(hours=8))  # 获取时区偏移量

    shanghai_time = datetime.datetime.fromtimestamp(timestamp, offset)  # 将时间戳转换为时区时间

    return shanghai_time.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间
