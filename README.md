# FastAPI

## 介绍

+ Python Web框架 [FastAPI](https://fastapi.tiangolo.com/zh/) 📖

+ VUE + FastAPI 实现学生选课系统（尝试中......😝）
+ 第一次做前后端分离的项目，希望可以完成！！！😁

## 版本

+ `V1.0` FastAPI学习
+ `V2.0` 搭建FastAPI脚手架
+ `V2.1` 创建所需的表
+ `V2.2` 已成功调试Mysql、Sqlite, 未调试Postgresql
+ `V2.3` 初始化表数据(调试)
+ `V2.4` 优化创建表问题
+ `V2.5` 初始化所有表数据
+ `V2.6` 封装日志模块

1. `V2.7` 优化代码
2. `V3.0` 接口的调试

## 安装

1. 配置Python3.6(及以上)的虚拟环境

2. 安装运行所需的包

   ```python
   pip install fastapi
   pip install uvicorn
   pip install SQLAlchemy
   
   # mysql
   pip install mysqlclient
   
   # 或者
   pip install requirements.txt
   ```

3. 启动服务（未做）

    + 进入到 `app02` 项目下
    + 找到 `main.py` 右键运行

   > 接口文档：http://127.0.0.1:8000/docs

## 文档目录

```sh
|-- app
	|-- core					
		|-- init.py			    # 核心内容
		|-- config.py			# 配置文件
		|-- logger.py			# 日志模块
 	|-- db						
 		|-- init.py			    # 数据库相关
		|-- base.py				# 配置需要创建的表
		|-- base_class.py		# 自动生成 表名
		|-- init_db.py			# 创建base中的表
		|-- session.py			# 创建数据库连接会话
	|-- initial_data
    	|-- init.py			    # 初始化表数据
    	|-- data_core.py		# SQLAlchemy_Core 的数据
    	|-- data_orm.py			# SQLAlchemy_ORM 的数据
    	|-- init_data.py		# 两种初始化表数据的方式
    |-- logs                    # 日志模块(自动生成)
        |-- log                 # 当前时间段暂存的日志
        |-- 2021-10-06_23-46-45.log			    
        |-- 2021-10-06_23-46-47.log			    
        |-- 2021-10-06_23-46-49.log			    
	|-- models                  
		|-- init.py			    # ORM模型
		|-- admin.py			# 管理员表
		|-- control.py			# 控制表
		|-- course.py			# 课程表
		|-- department.py		# 院系表
		|-- major.py			# 专业表
		|-- selectCourse.py		# 选课表
		|-- student.py			# 学生表
		|-- teacher.py			# 教师表
		|-- user.py				# 调试表
	|-- schemas                 
		|-- init.py			    # 通过api接收数据的数据验证
		|-- admin.py			# 管理员数据验证
		|-- control.py			# 控制表数据验证
		|-- course.py			# 课程表数据验证
		|-- department.py		# 院系表数据验证
		|-- major.py			# 专业表数据验证
		|-- selectCourse.py		# 选课表数据验证
		|-- student.py			# 学生表数据验证
		|-- teacher.py			# 教师表数据验证
		|-- user.py				# 调试表数据验证
	|-- test   
    	|-- init.py				# 测试文件夹
    	|-- db_init				
    		|-- init.py			# 调试初始化表数据
    		|-- data_core.py	# 需要初始化数据
    		|-- initial_data.py	# 初始化的方法
    	|-- logger
    	    |-- init.py			# 调试日志模块
    	    |-- logger_01.py	# 创建单个日志
    	    |-- logger_02.py	# 创建日志文件夹
    	    |-- logger_03.py	# 创建日志文件夹(自动删除)
	|-- init.py
	|-- main.py					# 主程序
	|-- requirements.txt		# 所需的包
	|-- sql_app.db              # sqlite数据库
```

