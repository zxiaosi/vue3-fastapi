#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/24 19:40
# @Author : 小四先生
# @desc : 数据
from models.user import User

userData = [
    User(user_id='4', full_name='小二', password='123'),
    User(user_id='5', full_name='小三', password='123')
]

data = [
    {'user_id': 6, 'full_name': '小刘', 'password': '123'},
    {'user_id': 7, 'full_name': '小赵', 'password': '123'},
]
