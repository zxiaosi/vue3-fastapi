#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/28 17:20
# @Author : zxiaosi
# @desc : 存储在Reids中的数据模板
import abc
from datetime import datetime

from redis_om import get_redis_connection, Field, HashModel, JsonModel, EmbeddedJsonModel

from core.config import settings

# 参考文档 https://github.com/redis/redis-om-python/blob/main/docs/fastapi_integration.md

REDIS_CONNECTION = get_redis_connection(url=settings.REDIS_URI, decode_responses=True)  # redis 连接
GLOBAL_KEY_PREFIX = "redis-om"  # redis 中 key 前缀


class RequestIp(HashModel):
    """ Redis请求IP信息(重复请求)"""
    num: int = Field(index=True, full_text_search=True)

    class Meta:
        database = REDIS_CONNECTION
        global_key_prefix = GLOBAL_KEY_PREFIX
        model_key_prefix = "request"  # redis 中 ORM对象 前缀 (默认是 路径+类名)


class LocalResource(EmbeddedJsonModel):
    """ Redis资源信息 """
    id: int
    name: str
    level: str
    pid: str
    icon: str | None
    menu_url: str | None
    request_url: str | None
    permission_code: str | None
    is_deleted: int
    create_time: datetime
    update_time: datetime

    class Meta:
        database = get_redis_connection(url=settings.REDIS_URI, decode_responses=True)
        global_key_prefix = "redis-om"
        model_key_prefix = "resource"  # redis 中 ORM对象 前缀 (默认是 路径+类名)


class LocalUser(JsonModel):
    """ Redis用户信息 """
    id: int = Field(index=True, full_text_search=True)
    name: str
    password: str
    avatar: str | None
    sex: int
    phone: str | None
    is_deleted: int
    create_time: datetime
    update_time: datetime
    # menu_urls: list[str] = Field(default=[])  # 用户可以访问的路由列表
    # request_urls: list[str] = Field(default=[])  # 用户可以请求的url列表
    # permission_codes: list[str] = Field(default=[])  # 用户可以访问的权限列表
    resources: list[LocalResource] = Field(default=[])  # 用户可以访问的资源列表

    class Meta:
        database = REDIS_CONNECTION
        global_key_prefix = GLOBAL_KEY_PREFIX
        model_key_prefix = "user"  # redis 中 ORM对象 前缀 (默认是 路径+类名)
