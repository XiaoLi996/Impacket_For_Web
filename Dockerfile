# 使用带有Python的Alpine Linux作为基础镜像
FROM python:3.10-alpine

# 设置工作目录
WORKDIR /Impacket_For_Web

# 将当前目录的内容复制到容器的工作目录
COPY . .

# 安装必要的依赖项
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口8000
EXPOSE 8000

# 设置启动命令
CMD ["python3", "main.py"]
