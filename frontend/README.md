## Vue-Manage-System

## 版本

+ `V1.0` 初始化项目
+ `V1.1` 调试了接口(测试页面)&&引入阿里的图标
+ `V1.2` 测试数据的增删改查已完成
+ `V1.3` 添加了院系表的增删改查，以及其相关字段的验证规则，添加了额外功能排序

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
   >密码：123123

## 项目截图

+ 登录界面（待定）

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/frontend-login.png)

+ 后台界面（待定）

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/frontend-%E5%90%8E%E5%8F%B0.png)

## 项目目录

```sh
|-- frontend
  |-- public					# 输出文件              
	|-- src						# 核心文件
	|-- index.html				# Vue配置文件
	|-- LICENSE			    	# Vue-Manage-System开源证书
	|-- index.html				# Vue配置文件
	|-- package-lock.html 
	|-- package.html    		# 安装的包
	|-- README.md       		# 文档说明
	|-- vite.config.js  		# vite配置
	
```



## 常见错误

### `npm run dev` 报错

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

