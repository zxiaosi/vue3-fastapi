const TokenKey = "Authorization$://"; //授权码
/*
 * 获取getItem
 * */
export function getLocal(Key?: string | undefined) {
  let local = localStorage.getItem(Key ? Key : TokenKey);
  try {
    if (local) return JSON.parse(local);
  } catch (e) {
    return local || null;
  }
}

/*
 * 设置setItem
 * */
export function setLocal(Key?: string, params?: any) {
  if(params instanceof Object) params = JSON.stringify(params);
  return localStorage.setItem(Key ? Key : TokenKey, params);
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