#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/3/4 15:21
# @Author : zxiaosi
# @desc : 根据ip获取地址
import re
from urllib import request
from ipaddress import ip_address

from utils import IpError


def verify_ip(ip):
    """ 验证ip格式是否正确 """
    try:
        return str(ip_address(ip))
    except Exception as e:
        raise IpError(f'错误的IP格式！ -- {e}')


def by_ip_get_address(ip) -> str:
    """ 根据ip获取地址 """
    verify_ip(ip)

    req = request.Request(f"http://ip.ws.126.net/ipquery?ip=${ip}")
    response = request.urlopen(req).read().decode('gbk')  # 获取响应

    handle_address = re.findall(r'"([^"]*)"', response)
    if handle_address:
        return handle_address[0] + handle_address[1]
    else:
        return '广东省广州市'
