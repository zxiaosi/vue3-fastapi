#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:02
# @Author : 小四先生
# @desc : 配置文件
from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator


# 配置信息
class Settings(BaseSettings):
    # api 前缀
    API_V1_STR: str = "/api/v1"

    # 跨域请求
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:3000", "http://localhost:8000"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # 接口文档的 名字
    PROJECT_NAME = "FastAPI"
    # 接口文档的 描述
    PROJECT_DESCRIPTION = "FastAPI接口"
    # 接口文档的 版本
    PROJECT_VERSION = "3.0"

    # 数据库链接
    # SQLALCHEMY_DATABASE_URI = "mysql://user:password@hostname/dbname?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"  # (可开启下面的多线程)
    # Sqlite多线程 (False关闭单线程 | True 开启单线程)
    SQLALCHEMY_DATABASE_THREAD = False
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/elective_system?charset=utf8"  # (关闭 db/session 下的多线程)
    # 数据库日志 (可看到创建表、表数据增删改查的信息)
    SQLALCHEMY_DATABASE_ECHO = False

    # 日志文件夹名
    LOGGER_FOLDER = "logs"
    # 日志文件名 (时间格式)
    LOGGER_NAME = '{time:YYYY-MM-DD_HH-mm-ss}.log'
    LOGGER_ENCODING = 'utf-8'
    LOGGER_LEVEL = 'DEBUG'  # ['DEBUG' | 'INFO']
    # 按 时间段 切分日志
    LOGGER_ROTATION = "1 minute"  # ["500 MB" | "12:00" | "1 week"]
    # 日志保留的时间, 超出将删除最早的日志
    LOGGER_RETENTION = "3 minute"  # ["1 days"]


# 初始化配置信息
settings = Settings()
