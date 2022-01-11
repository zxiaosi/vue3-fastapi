
/**
 * 通过id得到name
 * @param {*} id 外键
 * @param {*} data 外键对应的表数据
 * @returns 
 */
export const byIdGetName = (id, data) => {
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
