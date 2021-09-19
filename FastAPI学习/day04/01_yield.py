#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/12 19:10
# @Author : 小四先生
# @desc :
def fun():
    try:
        print(1)
        db = 'SessionLocal()'  # db也可被赋予变量
        yield db
    finally:
        print('3')


for i in fun():
    print(i)
    print('2')
