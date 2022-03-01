const TokenKey = "Authorization$://"; //授权码
/*
 * 获取getItem
 * */
export function getLocal(key?: string) {
  return localStorage.getItem(key ? key : TokenKey) as any;
}

/*
 * 设置setItem
 * */
export function setLocal(key: string | undefined, params: any) {
  return localStorage.setItem(key ? key : TokenKey, params);
}

/*
 * 移除removeItem
 * */
export function removeLocal(key?: string) {
  return localStorage.removeItem(key ? key : TokenKey);
}

/*
 * getBaseFile64
 * */
export async function getBaseFile64(file: Blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });
}
