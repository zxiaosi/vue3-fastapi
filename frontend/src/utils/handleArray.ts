import type { FormData } from "@/types/table";

/**
 * 加工数组
 * @param data 数组
 * @param keyName 想要返回的 key 名
 * @returns value 列表
 */
export const valueList = (data: any[], keyName: string): string[] => {
  return data.map((item: any) => {
    return item[keyName].toString();
  });
};

/**
 * 通过id得到name
 * @param {*} id 外键
 * @param {*} data 外键对应的表数据
 * @returns 对应的name
 */
export const byIdGetName = (id: string, data: FormData[]) => {
  if (!id) {
    return null;
  }
  for (let i = 0, len = data.length; i < len; i++) {
    let item = data[i];
    if (item.id == id) {
      return item.name;
    }
  }
  return null;
};
