# Python版本
FROM python:3.9

# 工作路径
WORKDIR /code

# 方便下面使用缓存加载
COPY ./requirements.txt /code/requirements.txt

# 使用缓存下载安装包
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 使用缓存下载安装包(镜像)
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=1000 --no-cache-dir --upgrade -r /code/requirements.txt

# docker部署(https://fastapi.tiangolo.com/zh/deployment/docker/)
# .表示同级目录下
COPY . /code/

# 启动命令
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# main.py启动命令
CMD ["python", "main.py"]