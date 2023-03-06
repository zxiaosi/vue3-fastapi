## Vue3+ FastAPI Demo

### 1.项目目录

```sh
-- 服务器
	-- ...
	-- root
	-- opt
		-- containerd 
		-- docker 								# 存放docker容器配置
			-- mysql							# mysql 配置
			-- nginx							# nginx 配置
				-- conf.d						
					-- default.conf				 # nginx 配置 【重要】
				-- html							# 存放打包后的文件 【重要】
				-- ...
			-- redis							# redis
			-- demo								# 项目配置
				-- frontend						# 前端
				-- backend						# 后端
					-- Dockerfile				# 构建镜像【重要】 
				-- docker-compose.yml			 # docker-compose 【重要】
				-- ...
			-- ...
```



### 2. Dcoker浅学

+ [Ubuntu18.4 内使用 Docker-Compose](https://zxiaosi.com/archives/ae105511.html)
+ [Docker 部署项目](https://zxiaosi.com/archives/b32496b.html)

### 3. 前端部署

+ 将 `frontend/src/assets/js/global.ts` 文件中 `API_URL_PRODUCTION` 字段改为服务器 `IP`

+ 修改 `frontend/src/request/https.ts` 文件中的 `isDev` 字段为 `false`

  ```javascript
  // 是否是开发环境
  // const isDev: boolean = true;
  const isDev: boolean = false;
  ```

+ 运行 `npm run build` 命令打包文件

+ 将 `frontend/dist` 中的文件上传到服务器 `/opt/docker/nginx/html` 文件夹下

### 4. 后端部署

+ 修改 `backend/core/config.py` 中的 `IS_DEV` 字段为 `false`

  ```sh
  # IS_DEV = True  # 是否开发环境
  IS_DEV = False  # 是否开发环境
  ```
  
+ 修改 `backend/core/config.py` 中的部分字段

+ 使用 `Docker` 创建网络桥段 

  ```sh
  # docker network ls 查看网络桥段
  # docker network create 桥段名 
  
  # app 为 docker-compose.yml 中定义的桥段名
  docker network create app
  ```

+ 运行 `/opt/docker/demo` 文件下的 `docker-compose.yml`

  ```sh
  docoker-compose -f /opt/docker/demo/docker-compose.yml up -d
  ```

+ 创建名为 `demo` 的数据库, 并导入 `demo.sql`

### 5. Nginx 配置 ( `/nginx/conf.d/default.conf` )

```sh
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        try_files $uri $uri/ /index.html; # 防止页面刷新404
    }

    location /api {
        client_max_body_size 5m;
        proxy_pass http://fastapi:8000; # 这里 localhost -> 对应的容器名
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr; 
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    }
    
    # 可选
    location /api/docs { # docs 文档地址
        proxy_pass http://fastapi:8000/docs;
    }

    location /api/redoc { # redoc 文档地址
        proxy_pass http://fastapi:8000/redoc;
    }

    location /openapi.json { # openapi 地址 (如果代理上述文档地址, 请务必添加 openapi 的代理)
        proxy_pass http://fastapi:8000/openapi.json;
    }

    ...
}

```

