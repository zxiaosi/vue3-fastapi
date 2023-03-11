const TokenKey = "Authorization$://"; //授权码
/*
 * 获取getItem
 * */
export function getLocal(Key?: string | undefined) {
  let local = localStorage.getItem(Key ? Key : TokenKey) as any;
  return local ? JSON.parse(local) : null;
}

/*
 * 设置setItem
 * */
export function setLocal(params: any, Key?: string) {
  return localStorage.setItem(Key ? Key : TokenKey, JSON.stringify(params));
}
/*
 * 移除removeItem
 * */
export function removeLocal(key?: string) {
  return localStorage.removeItem(key ? key : TokenKey);
}

/*
 * 清空所有Item
 * */
export function clearLocal() {
  return localStorage.clear();
}