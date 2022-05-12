## Vue3+ElementPlus+Vite

## 版本

+ `V1.0` 初始化项目
+ `V1.1` 调试了接口(测试页面)&&引入阿里的图标
+ `V1.2` 测试数据的增删改查已完成
+ `V1.3` 添加了院系表的增删改查，以及其相关字段的验证规则，添加了额外功能排序
+ `V1.4` 首页数据更改，待办事项可以添加(临时数据)
+ `V1.5` 添加了专业表的增删改查
+ `V1.6` 调试了专业表中下拉框
+ `V1.6` 添加了教师表
+ `V1.7` 添加了学生表、课程表、选课表
+ `V1.8` 重构代码
+ `V1.9` 封装了部分组件
+ `V2.0` 重构表格代码
+ `V2.1` 封装了部分方法,重构表格组件
+ `V2.1` 修改了校验规则
+ `v2.2` 修复打包出现的小问题
+ `v2.3` 部署成功
+ `v2.4` 添加加载效果
+ `v2.5` 通过vuex优化取数据的方式
+ `v2.6` 优化请求方式&&部分数据添加到redis中
+ `v2.7` 首页数据添加到redis中
+ `v2.8` 加入TS
+ `v2.9` 实现图片上传
+ `v3.0` 分离文件(vue与ts分离)
+ `v3.1` 简单实现权限管理
+ `v3.2` 整理代码
+ `v3.3` 语言详情更换为Github公共API
+ `v3.4` 简单实现学生选课
+ `v3.5` 简单实现教师讲授课程

## 安装

1. 进到 `frontend` 目录下

2. `npm install` 安装所需的包

3. 启动服务

   + `npm run dev` 运行项目
   + <font color="red">报错见下面</font>

   >服务接口：http://localhost:3000/
   >
   >用户名：admin
   >
   >密码：123

## 项目截图

+ 登录界面（待定）

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/frontend-login.png)

+ 后台界面（待定）

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/frontend-%E5%90%8E%E5%8F%B0.png)

## 项目目录

```sh
|-- frontend
  |-- dist					  # 输出文件              
	|-- src					  # 核心文件
      |-- api                   # 接口
      |-- assets                # 静态文件
      |-- commponents           # 组件
      |-- request               # axios请求
      |-- router                # 路由
      |-- stores                # 状态管理
      |-- types                 # 公用接口
      |-- utils                 # 工具类
      |-- views                 # 页面
      |-- App.vue               # app
      |-- main.ts               # 主文件
	|-- index.html			   # 首页
  |-- env.d.ts                  # 
	|-- package-lock.json       # 包版本锁
	|-- package.json    	   # 安装的包
	|-- README.md       	   # 文档说明
  |-- tsconfig.json             # ts配置
  |-- tsconfig.vite-config.json # 兼用node与vite
	|-- vite.config.js          # vite配置
	
```



## 常见错误

### 1. `npm run dev` 报错

+ 内容如下

  ```sh
  > vue-manage-system@5.1.0 dev
  > vite
  
  events.js:377
        throw er; // Unhandled 'error' event
        ^
  
  Error: spawn D:\Vscode\Vue-Manage-System\node_modules\esbuild\esbuild.exe ENOENT
      at Process.ChildProcess._handle.onexit (internal/child_process.js:274:19)
      at onErrorNT (internal/child_process.js:469:16)
      at processTicksAndRejections (internal/process/task_queues.js:82:21)
  Emitted 'error' event on ChildProcess instance at:
      at Process.ChildProcess._handle.onexit (internal/child_process.js:280:12)
      at onErrorNT (internal/child_process.js:469:16)
      at processTicksAndRejections (internal/process/task_queues.js:82:21) {
    errno: -4058,
    code: 'ENOENT',
    syscall: 'spawn D:\\Vscode\\Vue-Manage-System\\node_modules\\esbuild\\esbuild.exe',
    path: 'D:\\Vscode\\Vue-Manage-System\\node_modules\\esbuild\\esbuild.exe',
    spawnargs: [ '--service=0.12.9', '--ping' ]
  }
  ```

+ 错误原因：`vite` 安装失败

+ 解决措施：输入下面命令 `node .\node_modules\esbuild\install.js`，重新运行 `npm run dev`

### 2. `npm run dev` 报错

+ 内容如下

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/%E6%8A%A5%E9%94%992.png)

+ 错误原因：`端口号被占用`
+ 解决措施：关闭其他占用 `3000`端口号的应用，重新运行 `npm run dev`

