# FastAPI

## 版本

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

## 安装

1. 配置Python3.9(及以上)的虚拟环境

2. 安装运行所需的包

   ```python
   pip install fastapi
   pip install uvicorn
   pip install loguru
   pip install SQLAlchemy
   pip install python-jose
   pip install passlib
   pip install bcrypt
   
   # mysql
   pip install mysqlclient
   
   # 或者
   pip install requirements.txt
   ```


3. 启动服务

    + 进入到 `backend` 项目下
    + 找到 `main.py` 右键运行
    + `core/config` 配置文件(默认使用了SQLite,可以配置MySQL)

   > 接口文档：http://127.0.0.1:8000/docs

## 项目截图

+ 成功运行的图片

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/image-20211021164103094.png)

+ 接口图

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/backend-%E6%8E%A5%E5%8F%A3.png)

## 项目目录

```sh
|-- backend
    |-- api					    # 接口文档
        |-- __init__.py	        
        |-- deps.py	            # 获取数据库连接对象
        |-- api_v1              # api版本1
            |-- __init__.py	       	        
            |-- api.py	       	# 接口汇总       
            |-- endpoints	    # 接口
                |-- __init__.py	           
                |-- users.py	# 用户表接口
                         
	|-- core					# 核心内容
		|-- __init__.py			    
		|-- config.py			# 配置文件
		|-- security.py		    # 安全配置
		
	|-- crud					# 数据库的增删改查操作
		|-- __init__.py			# 抛出操作表数据文件中的类
		|-- base_class.py			    # 封装数据库增删改查方法
		|-- crud_user.py		# 用户表--增删改查方法
		
 	|-- db						# 数据库相关
 		|-- __init__.py			# 抛出数据库生成、删除表的方法
		|-- base_class.py				# 配置需要创建的表
		|-- base_class.py		# 自动生成 表名
		|-- init_db.py			# 创建和删除base中的表
		|-- session.py			# 创建数据库连接会话
		
	|-- initial_data            # 初始化表数据
    	|-- __init__.py			# 抛出初始化表数据的两种方法
    	|-- data_core.py		# 所有数据
    	|-- data_orm.py			# 加工 data_core 中的数据
    	|-- init_data.py		# 两种初始化表数据的方式
    	
    |-- logs                    # 日志模块(自动生成)
        |-- log                 # 当前时间段暂存的日志
        |-- 2021-10-06_23-46-45.log			    
        |-- 2021-10-06_23-46-47.log			    
        |-- 2021-10-06_23-46-49.log		
        	    
	|-- models                  # ORM模型映射
		|-- __init__.py			# 抛出ORM模型对象
		|-- admin.py			# 管理员表
		|-- control.py			# 控制表
		|-- course.py			# 课程表
		|-- department.py		# 院系表
		|-- major.py			# 专业表
		|-- selectCourse.py		# 选课表
		|-- student.py			# 学生表
		|-- teacher.py			# 教师表
		|-- user.py				# 调试表
		
	|-- schemas                 # Pydantic数据验证
		|-- __init__.py			# 抛出Pydantic数据验证
		|-- admin.py			# 管理员表数据验证
		|-- control.py			# 控制表数据验证
		|-- course.py			# 课程表数据验证
		|-- department.py		# 院系表数据验证
		|-- major.py			# 专业表数据验证
		|-- selectCourse.py		# 选课表数据验证
		|-- student.py			# 学生表数据验证
		|-- teacher.py			# 教师表数据验证
		|-- user.py				# 调试表数据验证
		
	|-- utils                   # 封装工具
	    |-- __init__.py		    # 抛出工具类
	    |-- logger.py		    # 封装日志模块
	    |-- response_code.py	# 封装统一的响应JSON数据
		
	|-- test                    # 测试文件夹
    	|-- __init__.py				
    	|-- db_init				# 调试初始化表数据
    		|-- __init__.py			
    		|-- data_core.py	# 需要初始化数据
    		|-- initial_data.py	# 初始化的方法
    		
    	|-- logger              # 调试日志模块
    	    |-- __init__.py			
    	    |-- logger_01.py	# 创建单个日志
    	    |-- logger_02.py	# 创建日志文件夹
    	    |-- logger_03.py	# 创建日志文件夹(自动删除)
    	    |-- logger_04.py	# 创建日志(单线程)
    	    
	|-- __init__.py
	|-- main.py					# 主程序
	|-- requirements.txt		# 所需的包
	|-- sql_app.db              # sqlite数据库
```

