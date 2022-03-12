/**
 * 点击后鼠标移开恢复按钮默认样式
 */
export const clickRecover = (event: MouseEvent) => {
  let target: any = event.target;
  // (如果按钮没有加icon图标的话，target.nodeName == "I"可以去掉)
  if (target.nodeName == "I" || target.nodeName == "SPAN") {
    target = target.parentNode;
  }
  target.blur();
};
