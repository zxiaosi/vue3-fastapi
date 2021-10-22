#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 17:02
# @Author : 小四先生
# @desc : 配置文件
from typing import List, Union, Optional

from pydantic import BaseSettings, AnyHttpUrl, validator, HttpUrl
from core.logger import MyLogger


# 配置信息
class Settings(BaseSettings):
    # api 前缀
    API_V1_STR: str = "/api/v1"

    # 跨域请求
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:3000"]

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
    SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"  # (可开启 db/session 下的多线程)
    # SQLALCHEMY_DATABASE_URI = "mysql://user:password@hostname/dbname?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/elective_system?charset=utf8" # (关闭 db/session 下的多线程)
    # 数据库日志 (可看到创建表、表数据增删改查的信息)
    SQLALCHEMY_DATABASE_ECHO = False

    # 日志文件夹名
    LOGGER_FOLDER = "logs"
    # 临时日志文件名 (必填)
    LOGGER_NAME = "log"
    # 日志等级 (默认值为 "debug")
    LOGGER_LEVER = "debug"  # debug | info [ warning | error | critical ]
    # 日志时间格式 (默认值带毫秒)
    LOGGER_DATEFMT = '%Y-%m-%d %H:%M:%S'
    # 日志格式 (下面就是默认值)
    LOGGER_FMT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    # 将日志输出到控制台
    LOGGER_CONSOLE = True
    # 按 时间段 切分日志 (默认值为 "D")
    LOGGER_WHEN = "M"  # [S:秒 | M:分钟 | H: 小时 | D:天 | W: 周(0 = Monday) | midnight: 午夜]
    # 日志保留的最大个数, 超出将删除最早的日志
    LOGGER_BACKCOUNT = 3


# 初始化配置信息
settings = Settings()

# 初始化日志
logger = MyLogger(
    folderName=settings.LOGGER_FOLDER,
    tempName=settings.LOGGER_NAME,
    # level=settings.LOGGER_LEVER,
    datefmt=settings.LOGGER_DATEFMT,
    # fmt=settings.LOGGER_FMT,
    # console=settings.LOGGER_CONSOLE,
    when=settings.LOGGER_WHEN,
    backCount=settings.LOGGER_BACKCOUNT
)
