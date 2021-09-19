# FastAPI

## 介绍
+ Python Web框架 [FastAPI](https://fastapi.tiangolo.com/zh/) 📖

+ VUE + FastAPI 实现学生选课系统（尝试中......😝）
+ 第一次做前后端分离的项目，希望可以完成！！！😁

## 安装

1. 配置Python3.6(及以上)的虚拟环境

2. 安装运行所需的包

   ```python
   pip install fastapi
   pip install uvicorn
   pip install SQLAlchemy
   
   # 或者
   pip install requirements.txt
   ```

3. 启动服务（未做）

   + 进入到 `app` 项目下
   + 找到 `main.py` 右键运行

   >接口文档：http://127.0.0.1:8000/docs

## 文档目录

```sh
|-- app
	|-- core					# 核心内容
		|-- init.py			    
		|-- config.py			# 配置文件
 	|-- db						# 数据库
 		|-- init.py			    
		|-- base.py				# 配置创建的表
		|-- base_class.py		# 自动生成 表名
		|-- session.py			# 创建数据库连接会话
	|-- models
		|-- init.py			    
		|-- administrator.py	# 管理员表
		|-- control.py			# 控制表
		|-- course.py			# 课程表
		|-- department.py		# 院系表
		|-- major.py			# 专业表
		|-- selectCourse.py		# 选课表
		|-- student.py			# 学生表
		|-- teacher.py			# 教师表
		|-- user.py				# 调试表
	|-- init.py
	|-- main.py					# 主程序
	|-- requirements.txt		# 所需的包
```

