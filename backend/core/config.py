#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:02
# @Author : zxiaosi
# @desc : 配置文件
import secrets
from typing import Union, List
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_DESC: str = "所有接口汇总"  # 描述
    PROJECT_VERSION: Union[int, str] = 4.0  # 版本

    API_PREFIX: str = "/api"  # 接口前缀

    CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000", "http://8.136.82.204:8001"]  # 跨域请求

    GLOBAL_ENCODING: str = 'utf-8'  # 全局编码

    # DATABASE_URI: str = "sqlite:///./sql_app.db"  # sqlite
    DATABASE_URI: str = "mysql://root:123456@localhost:3306/elective_system?charset=utf8"  # mysql
    DATABASE_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)

    REDIS_URI: str = "redis://:123456@localhost:6379/1"  # redis

    SECRET_KEY: str = secrets.token_urlsafe(32)  # 密钥
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # token过期时间: 60 minutes * 24 hours * 7 days = 7 days

    LOGGER_FOLDER: str = "logs"  # 日志文件夹名
    LOGGER_NAME: str = '{time:YYYY-MM-DD_HH-mm-ss}.log'  # 日志文件名 (时间格式)
    LOGGER_LEVEL: str = 'DEBUG'  # 日志等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "12:00"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]

    class Config:
        case_sensitive = True  # 区分大小写


settings = Settings()
