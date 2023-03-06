#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/6 1:22
# @Author : zxiaosi
# @desc : 用户角色表的增删改查
from crud.base import CRUDBase
from models import UserRole
from schemas import UserRoleIn


class CRUDUserRole(CRUDBase[UserRole, UserRoleIn, UserRoleIn]):
    pass


user_role_crud = CRUDUserRole(UserRole)
