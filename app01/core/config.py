#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/13 17:02
# @Author : 小四先生
# @desc : 配置文件
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = "FastAPI"
    PROJECT_DESCRIPTION = "FastAPI连接sqlite"
    PROJECT_VERSION = "1.0"
    SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"


settings = Settings()
