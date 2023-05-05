#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/28 18:48
# @Author : zxiaosi
# @desc : 创建会话, 创建与删除所有表, 初始化数据
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from models import Base, User, Role, Resource, UserRole, RoleResource
from common.custom_log import my_logger

# 文档中介绍了四种 创建会话 的方式: https://docs.sqlalchemy.org/en/20/orm/session_basics.html

# 创建表引擎
engine = create_engine(
    url=settings.DATABASE_URI,  # 数据库uri
    echo=settings.DATABASE_ECHO,  # 是否打印日志
    pool_pre_ping=True,  # 每次连接前都会检查连接是否有效
)

# 会话创建器
SessionLocal = sessionmaker(engine, expire_on_commit=False, autoflush=False)


def init_table(is_drop: bool = True):
    """ 创建 database 下的所有表 """
    if is_drop:
        drop_table()
    try:
        Base.metadata.create_all(engine)
        my_logger.info("创建表成功!!!")
    except Exception as e:
        my_logger.error(f"创建表失败!!! -- 错误信息如下:\n{e}")


def drop_table():
    """ 删除 database 下的所有表 """
    try:
        Base.metadata.drop_all(engine)
        my_logger.info("删除表成功!!!")
    except Exception as e:
        my_logger.error(f"删除表失败!!! -- 错误信息如下:\n{e}")


def init_data():
    """ 初始化表数据 """
    with SessionLocal() as session:
        user1 = User(name="admin", password="30780cc6f2e56945aaf9c9578c932e22")
        user2 = User(name="user", password="30780cc6f2e56945aaf9c9578c932e22", sex=1)
        user3 = User(name="guest", password="30780cc6f2e56945aaf9c9578c932e22", sex=2)
        role1 = Role(name="超级管理员", code="ROLE_ADMIN", description="管理员")
        role2 = Role(name="管理员", code="ROLE_USER", description="普通用户")
        role3 = Role(name="游客", code="ROLE_GUEST", description="普通用户")
        resource1 = Resource(name="仪表盘", level=1, pid=0, icon="VBr0B.png", menu_url="/dashboard", request_url="/",
                             permission_code="")
        resource2 = Resource(name="系统管理", level=0, pid=0, icon="VBr0B.png", menu_url="/system/index",
                             request_url="/system", permission_code="sys")
        resource3 = Resource(name="用户管理", level=1, pid=2, icon="VBclq.png", menu_url="/system/user",
                             request_url="/user", permission_code="sys:user")
        resource4 = Resource(name="用户列表", level=2, pid=3, request_url="/user/list", permission_code="sys:user:list")
        resource5 = Resource(name="新增用户", level=2, pid=3, request_url="/user/add", permission_code="sys:user:add")
        resource6 = Resource(name="编辑用户", level=2, pid=3, request_url="/user/update",
                             permission_code="sys:user:update")
        resource7 = Resource(name="角色管理", level=1, pid=2, icon="VBsBc.png", menu_url="/system/role",
                             request_url="/role", permission_code="sys:role")
        resource8 = Resource(name="资源管理", level=1, pid=2, icon="VBr0B.png", menu_url="/system/resource",
                             request_url="/resource", permission_code="sys:resource")
        resource9 = Resource(name="公告通知", level=1, pid=0, icon="VBr0B.png", menu_url="/notice",
                             request_url="/notice", permission_code="notice")
        resource10 = Resource(name="日志记录", level=1, pid=0, icon="VBr0B.png", menu_url="/log", request_url="/log",
                              permission_code="log")

        user_role1 = UserRole(user_id=1, role_id=1)
        user_role2 = UserRole(user_id=2, role_id=2)
        user_role3 = UserRole(user_id=3, role_id=3)
        role_resource1 = RoleResource(role_id=1, resource_id=1)
        role_resource2 = RoleResource(role_id=1, resource_id=2)
        role_resource3 = RoleResource(role_id=1, resource_id=3)
        role_resource4 = RoleResource(role_id=1, resource_id=4)
        role_resource5 = RoleResource(role_id=1, resource_id=5)
        role_resource6 = RoleResource(role_id=1, resource_id=6)
        role_resource7 = RoleResource(role_id=1, resource_id=7)
        role_resource8 = RoleResource(role_id=1, resource_id=8)
        role_resource9 = RoleResource(role_id=1, resource_id=9)
        role_resource10 = RoleResource(role_id=1, resource_id=10)
        role_resource11 = RoleResource(role_id=2, resource_id=1)
        role_resource12 = RoleResource(role_id=3, resource_id=1)

        session.add_all([
            user1, user2, user3,
            role1, role2, role3,
            resource1, resource2, resource3, resource4, resource5, resource6, resource7, resource8, resource9,
            resource10,
            user_role1, user_role2, user_role3,
            role_resource1, role_resource2, role_resource3, role_resource4, role_resource5, role_resource6,
            role_resource7, role_resource8, role_resource9, role_resource10, role_resource11, role_resource12
        ])

        session.commit()
