#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:02
# @Author : zxiaosi
# @desc : 配置文件
import secrets
from typing import Union, List
from pydantic import BaseSettings, AnyHttpUrl

project_desc = """
    🎉 管理员接口汇总 🎉
    ✨ 账号: admin ✨
    ✨ 密码: 123456 ✨
    ✨ 权限(scopes): admin ✨
"""


class Settings(BaseSettings):
    PROJECT_DESC: str = project_desc  # 描述
    PROJECT_VERSION: Union[int, str] = 5.0  # 版本
    BASE_URL: AnyHttpUrl = "http://127.0.0.1:8000"  # 开发环境

    API_PREFIX: str = "/api"  # 接口前缀
    STATIC_DIR: str = 'static'  # 静态文件目录
    GLOBAL_ENCODING: str = 'utf-8'  # 全局编码
    CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000", "http://8.136.82.204:8001"]  # 跨域请求

    SECRET_KEY: str = secrets.token_urlsafe(32)  # 密钥(每次重启服务密钥都会改变, token解密失败导致过期, 可设置为常量)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1  # token过期时间: 60 minutes * 24 hours * 1 days = 1 days

    REDIS_URI: str = "redis://:123456@localhost:6379/1"  # redis
    # DATABASE_URI: str = "sqlite+aiosqlite:///./sql_app.db?check_same_thread=False"  # Sqlite(异步)
    DATABASE_URI: str = "mysql+asyncmy://root:123456@localhost:3306/elective_system?charset=utf8"  # MySQL(异步)
    # DATABASE_URI: str = "postgresql+asyncpg://postgres:123456@localhost:5432/postgres"  # PostgreSQL(异步)
    DATABASE_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)

    LOGGER_DIR: str = "logs"  # 日志文件夹名
    LOGGER_NAME: str = '{time:YYYY-MM-DD_HH-mm-ss}.log'  # 日志文件名 (时间格式)
    LOGGER_LEVEL: str = 'DEBUG'  # 日志等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "12:00"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]

    # 权限数据表 (格式务必为 {'名称', '描述'})
    PERMISSION_DATA: List[dict] = [{'admin': '管理员权限'}, {'teacher': '教师权限'}, {'student': '学生权限'}]

    class Config:
        case_sensitive = True  # 区分大小写


settings = Settings()
