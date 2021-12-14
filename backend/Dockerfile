# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# docker部署(https://fastapi.tiangolo.com/zh/deployment/docker/)
# .表示同级目录下
COPY . /code/.

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
