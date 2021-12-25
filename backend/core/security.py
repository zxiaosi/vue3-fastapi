#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/10/19 19:49
# @Author : 小四先生
# @desc : 安全配置
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


# 生成token
def create_access_token(
        subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    生成token

    :param subject: 字典
    :param expires_delta: 有效时间
    :return: 字符串
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# 验证明文密码 vs hash密码
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码 vs hash密码

    :param plain_password: 明文密码
    :param hashed_password: hash密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


# 加密明文
def get_password_hash(password: str) -> str:
    """
    加密明文

    :param password: 明文密码
    :return:
    """
    return pwd_context.hash(password)


# https://www.cnblogs.com/CharmCode/p/14191112.html?ivk_sa=1024320u
# 解密token
def check_jwt_token(token, secret_key=pwd_context, algorithms=ALGORITHM) -> dict:
    try:
        payload = jwt.decode(token=token, secret_key=secret_key, algorithms=algorithms)
        print(payload)
    # 当然两个异常捕获也可以写在一起，不区分
    except ExpiredSignatureError as e:
        print("token过期")
    except JWTError as e:
        print("token验证失败")
    return payload
