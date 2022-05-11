// http://www.manongjc.com/detail/23-npfbicezsphbgyn.html
// https://blog.csdn.net/u012175183/article/details/123205887

/**
 * 合并相同数据，导出合并行所需的方法(只适合el-table)
 * @param {Array} dataArray el-table表数据源
 * @param {Array} mergeRowProp 合并行的列prop
 * @param {Array} sameRuleRowProp 相同合并规则行的列prop
 */
export function getSpanMethod(dataArray, mergeRowProp, sameRuleRowProp) {
  /**
   * 要合并行的数据
   */
  const rowspanNumObject = {};

  //初始化 rowspanNumObject
  mergeRowProp.map((item) => {
    rowspanNumObject[item] = new Array(dataArray.length).fill(1, 0, 1).fill(0, 1);
    rowspanNumObject[`${item}-index`] = 0;
  });

  //计算相关的合并信息
  for (let i = 1; i < dataArray.length; i++) {
    mergeRowProp.map((key) => {
      const index = rowspanNumObject[`${key}-index`];
      if (dataArray[i][key] === dataArray[i - 1][key]) {
        rowspanNumObject[key][index]++;
      } else {
        rowspanNumObject[`${key}-index`] = i;
        rowspanNumObject[key][i] = 1;
      }
    });
  }

  /**
   * 添加同规则合并行的数据
   */
  if (sameRuleRowProp !== undefined) {
    let k = Object.keys(rowspanNumObject).filter((key) => {
      if (!key.includes("index")) {
        return key;
      }
    })[0];
    for (let prop of sameRuleRowProp) {
      rowspanNumObject[prop] = rowspanNumObject[k];
      rowspanNumObject[`${prop}-index`] = rowspanNumObject[`${k}-index`];
      mergeRowProp.push(prop);
    }
  }

  /**
   * 导出合并方法
   */
  const spanMethod = function ({ row, column, rowIndex, columnIndex }) {
    if (mergeRowProp.includes(column["property"])) {
      const rowspan = rowspanNumObject[column["property"]][rowIndex];
      if (rowspan > 0) {
        return { rowspan: rowspan, colspan: 1 };
      }
      return { rowspan: 0, colspan: 0 };
    }
    return { rowspan: 1, colspan: 1 };
  };

  return spanMethod;
}
