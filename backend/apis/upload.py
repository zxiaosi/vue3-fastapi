#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/4/26 17:35
# @Author : zxiaosi
# @desc : 上传文件
import os
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.encoders import jsonable_encoder

from common.depends import GetDB, CheckCookie
from common.result import ResultSchema, Result
from common.route_log import LogRoute
from core.config import settings, FileDirEnum
from crud import user_crud
from common.custom_log import my_logger
from schemas import UserOut

router = APIRouter(route_class=LogRoute)


@router.post("/")
async def upload_file(db: GetDB, _user: CheckCookie, file: UploadFile = File(...)) -> ResultSchema[UserOut]:
    """
    接收上传的文件和表单数据，并保存到本地
    """
    user_obj = user_crud.get(db, _user.id)  # 获取最新用户信息, 防止两个人同时操作

    try:
        my_logger.info(f"用户 {user_obj.name} 正在上传图片...")
        suffix = Path(file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix, dir=FileDirEnum.AVATAR.value) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
        my_logger.info(f"用户 {user_obj.name} 上传图片 {tmp_file_name} 成功.")
        # if user_obj.avatar:
        #     os.remove(os.path.join(FileDirEnum.AVATAR.value, user_obj.avatar))  # 删除旧头像
    finally:
        file.file.close()

    try:
        user_obj = user_crud.update(db, user_obj, {"avatar": tmp_file_name})  # 更新数据库

        _user.update(**jsonable_encoder(user_obj))
        _user.save().expire(settings.REDIS_EXPIRE)  # 更新redis

        return Result.success(data=_user)
    except Exception as e:
        return Result.fail(msg="图片上传失败")
