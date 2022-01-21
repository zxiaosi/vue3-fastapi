#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:02
# @Author : zxiaosi
# @desc : 配置文件
import secrets
from typing import List
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    # 接口文档
    PROJECT_DESCRIPTION: str = "管理员、教师、学生接口汇总"  # 描述
    PROJECT_VERSION: str = "4.0"  # 版本
    PROJECT_DIR: str = "/"  # 接口文档路径, 默认是/docs
    PROJECT_SERVERS: List[dict] = [  # 环境配置(https://fastapi.tiangolo.com/zh/advanced/behind-a-proxy/)
                                      {"url": "http://127.0.0.1:8000", "description": "线上环境"},
                                      {"url": "http://127.0.0.1:8000/env", "description": "测试环境"},
                                  ],
    PROJECT_ADMIN_NAME: str = "Admin"  # 管理员
    PROJECT_ADMIN_DESCRIPTION: str = "管理员接口"
    PROJECT_TEACHER_NAME: str = "Teacher"  # 教师
    PROJECT_TEACHER_DESCRIPTION: str = "教师接口"
    PROJECT_STUDENT_NAME: str = "Student"  # 学生
    PROJECT_STUDENT_DESCRIPTION: str = "学生接口"

    # 接口前缀
    API_STR: str = "/api"

    # 跨域请求
    CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:3000", "http://localhost:8000",
                                      "http://8.136.82.204:80", "http://8.136.82.204:8001", "https://zxiaosi.net"]

    # token
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 加密密钥
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 过期时间: 60 minutes * 24 hours * 8 days = 8 days

    # 全局编码
    GLOBAL_ENCODING: str = 'utf-8'

    # 数据库
    # DATABASE_URI: str = "sqlite:///./sql_app.db"  # Sqlite链接
    # (开启MySQL 需注释 db/session 下Sqlite的多线程)
    # DATABASE_URI: str = "mysql://user:password@host:port/dbname?charset=utf8"
    DATABASE_URI: str = "mysql://root:123456@localhost:3306/elective_system?charset=utf8"
    DATABASE_ECHO: bool = False  # 数据库日志 (可看到创建表、表数据增删改查的信息)

    # redis
    # REDIS_URI: str = "redis://user:password@host:port/db"
    REDIS_URI: str = "redis://:123456@8.136.82.204:6379/1"

    # 日志
    LOGGER_FOLDER: str = "logs"  # 文件夹名
    LOGGER_NAME: str = '{time:YYYY-MM-DD_HH-mm-ss}.log'  # 文件名 (时间格式)
    LOGGER_LEVEL: str = 'DEBUG'  # 等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "12:00"  # 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间, 超出将删除最早的日志. 例如 ["1 days"]

    # 是否区分大小写
    class Config:
        case_sensitive = True


# 初始化配置信息
settings = Settings()
