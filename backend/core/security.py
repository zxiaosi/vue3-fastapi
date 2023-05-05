#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/31 16:23
# @Author : zxiaosi
# @desc : 加密密码
import base64
import hashlib
import time
from binascii import Error

import rsa

from core.config import settings
from common.custom_exc import WrongPublicKey

public_pem = b"""
-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAIRZg26Mu59Yr9nPd5gjmAspPUD3hT0Z6MmDwGbqm49IjdboNyt69RBI
UFGjqOGL7yE84pfbr48yL+7SxpJd9uDNFc7kO9zVOz+rgKBfn3kCDLyLrB7W6wH6
DsajiPK45iVoHz8pzp+ELwOcLmiuHsFycSMep8FmfVZHhYxrzNqFAgMBAAE=
-----END RSA PUBLIC KEY-----
"""  # 公钥

private_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICYAIBAAKBgQCEWYNujLufWK/Zz3eYI5gLKT1A94U9GejJg8Bm6puPSI3W6Dcr
evUQSFBRo6jhi+8hPOKX26+PMi/u0saSXfbgzRXO5Dvc1Ts/q4CgX595Agy8i6we
1usB+g7Go4jyuOYlaB8/Kc6fhC8DnC5orh7BcnEjHqfBZn1WR4WMa8zahQIDAQAB
AoGAeaaJn4CuKH5tTMhdBjOZWpDyY5fgGVSKW0fF/xMgH2iyL1pM86NWRDwjz5ad
8YsdJzD+mlTsnrOjyWJlYlOEs8FikbXiSB6Ji5arR5Ee8Vfw7Qy5NqvDO/FKGbnE
vX5YWW69GFErvz0rrrdMIyK+UgS1f9fkDBieaN1xTqoVXRUCRQCbe6/Z4L9SQioh
kpq3KpPS9LH7JbQ30+2Q1AMoN5D31ofCh4OeOlfL1k5ho2otBQSslUEiZIJ3usWD
VgTegEJXwFrilwI9ANnpQYYJGqJloP2fJkB4HVD04Fn4WN0vRCPMCOKyZN/twpA2
+PedVoz1xmxPwRG/rUBwHWvwBn1JVaN7QwJEXltlkLfP47+7ibxKoDX6l99f06ZC
BE9csLO5ZsKx+3X51Zgfy/pkJZPc5Wwil0egWowJhzGv67ExBE9DjTQRDufxP+kC
PQDK7pa+pCvRoKNUjamp0DI8+k8UelsHYMUsMQ71TvzyLRFMDGW+8x9vFlM6+urq
BH7ry30az+S7OFgwbtECRGqBh1+2SZzgJuHUNHML433D8Xd2/e7vj4o84Mt+VR0W
u59fcMDhQSvNNHqLP+KB/fT2bXO88pSzfE2ZMR5ivpA3rOdX
-----END RSA PRIVATE KEY-----
"""  # 私钥


def get_cookie_hash(field: str | dict) -> str:
    """ 加密 Cookie """
    sha256_dict = hashlib.sha256()
    sha256_dict.update((str(field) + str(time.time()) + settings.MD5_SALT).encode("utf-8"))
    return sha256_dict.hexdigest()


def get_password_hash(password: str) -> str:
    """ 加密明文密码 """
    md5_dict = hashlib.md5()
    md5_dict.update((password + settings.MD5_SALT).encode("utf-8"))
    return md5_dict.hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    """ 验证明文密码 与 加密后的密码 是否一致 """
    ciphertext = get_password_hash(password)
    return bool(ciphertext == hashed_password)


def generate_rsa_key():
    """ 生成公钥、私钥  - https://www.cnblogs.com/wangyingblock/p/15908056.html """
    public_key, private_key = rsa.newkeys(1024)  # 生成公钥和私钥

    public = public_key.save_pkcs1()  # 转换格式
    private = private_key.save_pkcs1()  # 转换格式

    with open('../public.pem', mode='wb') as f:  # 存储
        f.write(public)
    with open('../private.pem', mode='wb') as f:  # 存储
        f.write(private)


def rsa_encrypt_password(plaintext):
    """ rsa加密(base64转码) - https://www.cnblogs.com/wangyingblock/p/15908056.html """
    return base64.b64encode(rsa.encrypt(plaintext.encode('utf-8'), rsa.PublicKey.load_pkcs1(public_pem)))


def rsa_decrypt_password(ciphertext):
    """ rsa加密(base64解码) - https://www.cnblogs.com/wangyingblock/p/15908056.html """
    try:
        return rsa.decrypt(base64.b64decode(ciphertext), rsa.PrivateKey.load_pkcs1(private_pem)).decode('utf-8')
    except Error:
        raise WrongPublicKey()


if __name__ == '__main__':
    print(get_password_hash("123456"))

    # generate_rsa_key()
    # encrypt = rsa_encrypt_password('123456')
    # print(encrypt)
    # decrypt = rsa_decrypt_password(encrypt)
    # print(decrypt.decode('utf-8'))  # 使用之前必须先解码
