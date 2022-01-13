/**
 * 传入数据数据, 返回关系字段
 * @param {*} data 数据数组
 * @returns 返回关系字段
 */
export const storeData = (data) => {
  return data.map((item) => {
    return { id: item.id, name: item.name };
  });
}