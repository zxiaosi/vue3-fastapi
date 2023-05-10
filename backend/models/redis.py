#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/28 17:20
# @Author : zxiaosi
# @desc : 存储在Reids中的数据模板
import json
from datetime import datetime
from typing import Any

from redis_om import get_redis_connection, Field, HashModel, JsonModel, EmbeddedJsonModel, NotFoundError

from core.config import settings


class MyJsonModel(JsonModel):
    """ json模型 (解决中文乱码问题) """

    @classmethod
    def get(cls, pk: Any) -> "JsonModel":
        """ 重写get方法, 从redis中获取数据 """
        document = json.dumps(cls.db().json().get(cls.make_key(pk)), ensure_ascii=False)
        if document == "null":
            raise NotFoundError
        return cls.parse_raw(document.encode('raw_unicode_escape').decode('utf-8'))


# 参考文档 https://github.com/redis/redis-om-python/blob/main/docs/fastapi_integration.md

REDIS_CONNECTION = get_redis_connection(url=settings.REDIS_URI, decode_responses=True)  # redis 连接


class RequestIp(HashModel):
    """ Redis请求IP信息(重复请求)"""
    num: int = Field(index=True, full_text_search=True)

    class Meta:
        database = REDIS_CONNECTION
        global_key_prefix = settings.REDIS_GLOBAL_PREFIX  # redis 全局前缀
        model_key_prefix = "request"  # redis 中 ORM对象 前缀 (默认是 路径+类名)


class LocalResource(EmbeddedJsonModel):
    """ Redis资源信息 """
    id: int | None
    name: str | None
    level: str | None
    pid: str | None
    icon: str | None
    menu_url: str | None
    request_url: str | None
    permission_code: str | None
    is_deleted: int | None
    create_time: datetime | None
    update_time: datetime | None

    class Meta:
        database = REDIS_CONNECTION
        global_key_prefix = settings.REDIS_GLOBAL_PREFIX  # redis 全局前缀
        model_key_prefix = "resource"  # redis 中 ORM对象 前缀 (默认是 路径+类名)


class LocalUser(MyJsonModel):
    """ Redis用户信息 """
    id: int = Field(index=True, full_text_search=True)
    name: str | None
    password: str | None
    avatar: str | None
    sex: int | None
    phone: str | None
    version: int | None
    is_deleted: int | None
    create_time: datetime | None
    update_time: datetime | None
    role_name: str | None  # 用户角色名称
    permission_codes: list[str] = Field(default=[])  # 用户可以访问的权限code列表

    # resources: list[LocalResource] = Field(default=[])  # 用户可以访问的资源列表

    class Meta:
        database = REDIS_CONNECTION
        global_key_prefix = settings.REDIS_GLOBAL_PREFIX  # redis 全局前缀
        model_key_prefix = "user"  # redis 中 ORM对象 前缀 (默认是 路径+类名)
