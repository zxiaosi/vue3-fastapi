## redis

```sh
set "visit_num" 1
```

```sh
set "request_num" 1
```

>Github <font color="red">公开</font>仓库详情见 API: https://api.github.com/repos/user/repo/languages
>例如：https://api.github.com/repos/zxiaosi/Vue3-FastAPI/languages

```sh
rpush "language_details" {"title": "Python", "percentage": 45.4, "color": "#f1e05a"}

rpush "language_details" {"title":"Vue","percentage":44.3,"color":"#42b983"}

rpush "language_details" {"title": "JavaScript", "percentage": 8.7, "color": "#409EFF"}

rpush "language_details" {"title": "\u5176\u4ed6", "percentage": 1.6, "color": "#f56c6c"}
```

```sh
rpush "todo_list" {"title": "\u54e5\u65af\u62c9", "status": true}

rpush "todo_list" {"title": "\u725b\u7684", "status": true}

rpush "todo_list" {"title": "555", "status": true}

rpush "todo_list" {"title": "111", "status": true}
```

## nginx

```sh
server {
    listen       8001;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html/dist;
        index  index.html index.htm;
        try_files $uri $uri/ /index.html; # 防止页面刷新404
    }

    #error_page  404              /404.html;

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}

server {
    listen       8000;
    server_name  localhost;

    location /api {
        client_max_body_size 5m;
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
          
        #   指定允许跨域的方法，*代表所有
        add_header Access-Control-Allow-Methods *;

        #   预检命令的缓存，如果不缓存每次会发送两次请求
        add_header Access-Control-Max-Age 3600;
        #   带cookie请求需要加上这个字段，并设置为true
        add_header Access-Control-Allow-Credentials true;

        #   表示允许这个域跨域调用（客户端发送请求的域名和端口） 
        #   $http_origin动态获取请求客户端请求的域   不用*的原因是带cookie的请求不支持*号
        add_header Access-Control-Allow-Origin $http_origin;

        #   表示请求头的字段 动态获取
        add_header Access-Control-Allow-Headers 
        $http_access_control_request_headers;
         
        #   OPTIONS预检命令，预检命令通过时才发送请求
        #   检查请求的类型是不是预检命令
        if ($request_method = OPTIONS){
            return 200;
        }
    }
}
```

