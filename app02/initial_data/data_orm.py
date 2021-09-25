#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 20:48
# @Author : 小四先生
# @desc : SQLAlchemy_ORM_Initial 的数据
from app02.models.user import User

data = [
    User(full_name='小一', password='123'),
    User(full_name='小二', password='123')
]
