let modules = import.meta.glob("@/views/pages/**/*.vue"); // 获取 views/home/ 下的vue文件

export const iterateMenu = (data: any) => {
  let result: any = [];

  data.forEach((item: any, index: number) => {
    result.push({
      path: item.menu_url,
      meta: { title: item.name, icon: item.icon },
      component: modules[`/src/views/pages${uriToFileName(item.menu_url)}.vue`],
    })

    if (item.children) {
      let res = iterateMenu(item.children);
      if (res) result[index].children = res;
    }
  });

  return result;
}

/**
 * 获取路由对应的文件名 eg: /user => User /home/user => /home/User
 * @param uri 路由地址
 * @returns 文件名
 */
export const uriToFileName = (uri: string) => {
  let strList = uri.split("/");
  let fileName = strList[strList.length - 1];
  let prefix = uri.replace(fileName, "");
  return `${prefix + fileName[0]?.toUpperCase() + fileName?.slice(1)}`;
}

/**
 * 跳转页面
 * @param router 路由对象
 * @param path 跳转路径
 */
export const pageTo = (router: any, path: string) => {
  router.push(path);
}