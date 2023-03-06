import JSEncrypt from "jsencrypt";
import { PUBLIC_PEM } from "@/assets/js/global";

/**
 * 加密内容
 */
export function encryptContent(conent: string) {
  const encryptor = new JSEncrypt(); // 创建加密对象实例
  encryptor.setPublicKey(PUBLIC_PEM); // 设置公钥
  const encrypted = encryptor.encrypt(conent); // 对内容进行加密
  return String(encrypted);
}

/**
 * 解密内容(需要私钥,暂不可用)
 */
function decryptContent(content: string, pwd: string) {
  let decrypt = new JSEncrypt(); // encrypt对象

  let priKey = "xxx"; // 私钥 private.pem

  decrypt.setPrivateKey(priKey); // 设置私钥

  var uncrypted = decrypt.decrypt(content); // 解密内容

  return uncrypted == pwd;
}
