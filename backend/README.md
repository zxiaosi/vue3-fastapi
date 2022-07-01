# FastAPI

## 版本迭代

+ `V1.0` FastAPI学习
+ `V2.0` 搭建FastAPI脚手架
+ `V2.1` 创建所需的表
+ `V2.2` 已成功调试Mysql、Sqlite, 未调试Postgresql
+ `V2.3` 初始化表数据(调试)
+ `V2.4` 优化创建表问题
+ `V2.5` 初始化所有表数据
+ `V2.6` 封装日志模块
+ `V2.7` 封装多进程日志模块(线程锁)
+ `V2.8` 优化了目录结构
+ `V2.9` 优化代码&&调试了user表的增删查接口
+ `V3.0` 添加了防止跨域请求代码&&调试了接口
+ `V3.1` 去除了测试表的自增
+ `V3.2` 添加了department表的接口
+ `V3.3` 添加了major表的接口
+ `V3.4` 更新了major表接口的部分代码
+ `V3.5` 更换了日志模块(loguru)&&添加了后端数据验证
+ `V3.5` 添加了teacher表的接口
+ `V3.6` 添加了student表的接口
+ `V3.7` 添加了course表和selectCourse表的接口
+ `V3.8` 更新了所需的包
+ `V3.9` 修改了查询单个信息的数据
+ `V4.0` 删除了获取所有数据以及获取单个数据的方法
+ `V4.1` 修改了校验规则
+ `V4.1.1` 删除了整型和浮点型的正则校验规则
+ `v4.2` 尝试部署中。。。
+ `v4.3` 部署成功,修复了部分bug
+ `v4.4` 测试token
+ `v4.5` 调试token成功(admin, 123)
+ `v4.6` 重构FastAPI
+ `v4.7` 添加redis
+ `v4.8` 重构后端
+ `v4.9` 支持PostgreSQL,以及图片上传
+ `v5.0` 后台实现权限管理模块
+ `v5.1` 整理接口,简单实现权限管理模块
+ `v5.2` 调整数据库结构

## 安装

1. 配置<font color="red">Python3.9(及以上)</font>的虚拟环境

2. 安装运行所需的包

   ```python
   # 默认装了Mysql与ProgreSQL
   pip install requirements.txt
   
   # 或者
   pip install fastapi
   pip install uvicorn[fastapi]
   pip install loguru
   pip install SQLAlchemy
   pip install aioredis
   pip install python-jose
   pip install passlib
   pip install bcrypt
   pip install python-multipart
   pip install orjson
   
   # 使用Sqlite(异步), 请安装下面包
   pip install aiosqlite
   
   # 使用MySQL(异步), 请安装下面包
   pip install asyncmy
   
   # 使用ProgreSQL(异步), 请安装下面包
   pip install asyncpg
   ```


3. 启动服务

    + 进入到 `backend` 项目下
    + 找到 `main.py` 右键运行
    + `core/config` 配置文件(默认数据库是sqlite)

   > 接口文档：http://127.0.0.1:8000/docs

## 项目截图

+ 成功运行的图片

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/image-20211021164103094.png)

+ 接口图

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/backend-%E6%8E%A5%E5%8F%A3.png)

## 项目目录(待整理)

```sh
|-- backend

    |-- api					        # 接口
        |-- admin
            |-- __init__.py       	# 管理员接口       	             	                  
            |-- course.py	        # 课程表接口
            |-- department.py	    # 院系表接口
            |-- major.py	        # 专业表接口
            |-- index.py	        # 管理员首页    
            |-- elective.py	    # 选课表接口
            |-- student.py	        # 学生表接口
            |-- teacher.py	        # 教师表接口   
        |-- common                  
            |-- __init__.py       	# 共用接口 
            |-- login.py	        # 登录接口
            |-- redis_check.py	    # 检查redis是否连接成功
            |-- upload.py	        # 图片上传
        |-- __init__.py	         
        |-- deps.py	                # 依赖项
        |-- api_router.py	       	# admin接口汇总    
                         
	|-- core					
		|-- __init__.py			# 核心内容   
		|-- config.py			# 配置文件
		|-- security.py		    # 安全配置
		
	|-- crud
		|-- __init__.py			# 数据库的增删改查操作
		|-- base.py     		# 封装数据库增删改查方法
		|-- course.py	        # 课程表
		|-- department.py	    # 院系表
		|-- major.py		    # 专业表
		|-- elective.py     # 选课表
		|-- teacher.py		    # 教师表
		|-- student.py		    # 学生表
		
 	|-- db					
 		|-- __init__.py			# 初始数据库以及表数据
		|-- data.py		        # 所有数据
    	|-- init_data.py		# 两种初始化表数据的方式
		|-- init_db.py			# 创建和删除base中的表
		|-- session.py			# 创建数据库连接会话
    	|-- redis.py		    # 注册Redis
    	
    |-- logs                    # 日志模块(自动生成)
        |-- 2021-10-06_23-46-45.log			    
        |-- 2021-10-06_23-46-47.log			    
        |-- 2021-10-06_23-46-49.log		
        	    
	|-- models                  
		|-- __init__.py			# ORM模型映射
		|-- base.py		        # 自动生成 表名
		|-- index.py			# 管理员表
		|-- course.py			# 课程表
		|-- department.py		# 院系表
		|-- major.py			# 专业表
		|-- elective.py		# 选课表
		|-- student.py			# 学生表
		|-- teacher.py			# 教师表
		
	|-- register               
	    |-- __init__.py			# 注册中心
	    |-- cors.py			    # 注册跨域请求
	    |-- exception.py		# 注册全局异常
	    |-- middleware.py		# 注册请求响应拦截
	    |-- router.py		    # 注册路由
	    
	|-- schemas 
		|-- __init__.py			# 数据模型
		|-- admin.py			# 管理员表模型
		|-- common.py			# 公用表模型
		|-- course.py			# 课程表模型
		|-- department.py		# 院系表模型
		|-- login.py		    # 登录模型
		|-- major.py			# 专业表模型
		|-- result.py			# 返回数据模型
		|-- elective.py		# 选课表模型
		|-- student.py			# 学生表模型
		|-- teacher.py			# 教师表模型
		|-- todo.py			    # 待办模型
		|-- token.py			# token模型
		
	|-- utils                   # 工具
	    |-- __init__.py		    # 抛出工具类
	    |-- create_dir.py		# 创建文件夹类(位置勿动)
	    |-- custon_exc.py		# 自定义异常
	    |-- ip_address.py		# 根据ip获取位置
	    |-- logger.py		    # 日志模块
	    |-- permission_assign.py # 权限管理
	    |-- resp_code.py	    # 状态码
	
	|-- __init__.py
	|-- main.py					# 主程序
	|-- Dockerfile              # Dockerfile文件
	|-- README.md               # Readme文件
	|-- requirements.txt		# 所需的包
	|-- sql_app.db              # sqlite数据库
```

