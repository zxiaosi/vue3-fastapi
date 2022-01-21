# 学生选课系统

## 预览

+ [Vue3+Vite+ElementPlus](http://8.136.82.204:8001/)
+ [FastAPI接口预览](http://8.136.82.204:8000/)

## 介绍

+ Python Web框架 [FastAPI](https://fastapi.tiangolo.com/zh/) 📖
+ Vue3+ElementPlus+FastAPI 实现学生选课系统（尝试中......😝）
+ 第一次做前后端分离的项目，希望可以完成！！！😁

## 安装

+ **后端安装**：[FastAPI](https://fastapi.tiangolo.com/zh/) --> `backend` --> README.md（参考[CharmCode](https://www.charmcode.cn/category/FastAPI?page=1)）
+ **前端安装**：Vue3+ElementPlus+Vite --> `frontend` --> README.md (参考[Vue-Manage-System](https://github.com/lin-xin/vue-manage-system))

## 版本

+ `1.0` 测试数据的增删改查已完成
+ `1.1` 院系表的增删改查已完成（见`信息表格`）
+ `1.2` 首页仪表盘信息的优化
+ `1.3` 院系表的增删改查初步完成
+ `1.4` 整理代码
+ `1.5` 添加了教师表
+ `1.6` 添加了学生表、课程表、选课表
+ `1.7` 重构前端代码
+ `1.8` 封装组件，取出冗余代码
+ `1.9` 自定义表格组件
+ `2.0` 部署项目
+ `2.1` 重构FastAPI
+ `2.2` 配置nginx以及SSL证书(域名未备案，ssl证书未生效)
+ `2.3` 添加Redis

**TODO** 项目中加入TS 

## 开启服务

1. 后端

   + 进入到 `backend` 项目下
   + 找到 `main.py` 右键运行（建议用Pycharm启动）

   >接口文档：http://127.0.0.1:8000/

2. 前端

   + 进到 `frontend` 目录下
   + `npm run dev` 运行项目（建议用Vscode）

   >服务接口：http://localhost:3000/

3. 效果

+ 登录界面
  
  + `用户名`：`admin`

  + `密码`：`123123`
  
  + 如图
  
    ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/frontend-login.png)
  
+ 首页（假数据）

  ![home](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/home.png)
  
+ 数据的`增`

  ![add](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/add.gif)
  
+ 数据的`删`

  ![delete](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/delete.gif)

+ 数据的`改`

  ![update](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/update.gif)

+ 搜索数据

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/search.gif)

+ 多选删除

  ![selectedDelete](https://gitee.com/zxiaosi/image/raw/master/Project/Vue+FastAPI/selectedDelete.gif)
