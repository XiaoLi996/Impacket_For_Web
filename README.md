# Impacket_For_Web

实现让Impacket的几个横向模块可视化
本程序直接魔改Impacket的代码，实现Web API操作后加入前端，方便各位Hack大佬使用

# 特性
+ 免除死记各种参数
+ 可部署公网，多人操作
+ 实现程序内Socks隧道、不受工具、环境等限制

# 部署

暂时只支持Linux的Python3.10，其他平台如想使用可借助Docker，~~后期补充Docker教程~~已补充

```
# 拉取项目
git clone https://github.com/XiaoBai-12138/Impacket_For_Web.git
# 进入项目
cd Impacket_For_Web
# 安装依赖
pip3 install -r requirements.txt
# 运行程序
python3 main.py
# 访问程序
http://localhost:8000/Web/index.html
```

# Docker部署

```
# 以Ubuntu为例
# 安装Docker
apt install docker.io
# 拉取Ubuntu镜像并运行
docker run -itd -p 8000:8000 --name Impacket_For_Web ubuntu
# 进入容器
docker exec -it Impacket_For_Web bash
# 安装python3.10等必要环境
apt update && apt install python3.10 python3-pip git
# 拉取项目
git clone https://github.com/XiaoBai-12138/Impacket_For_Web.git
# 进入项目
cd Impacket_For_Web
# 安装依赖
pip3 install -r requirements.txt
# 运行程序
python3 main.py
# 访问程序
http://localhost:8000/Web/index.html
```


哈希传递：

![哈希传递](https://github.com/XiaoBai-12138/Impacket_For_Web/blob/main/images/哈希传递.jpg?raw=true)

设置代理：

![设置代理](https://github.com/XiaoBai-12138/Impacket_For_Web/blob/main/images/设置代理.jpg?raw=true)

# 特别说明

如果需要部署公网使用需要更改以下代码中的localhost为自己的公网IP
后续会在前端加入配置项

```
Web/index.html：119行
Web/settings.js：153、179行
```

![代码一](https://github.com/XiaoBai-12138/Impacket_For_Web/blob/main/images/代码1.jpg?raw=true)
![代码二](https://github.com/XiaoBai-12138/Impacket_For_Web/blob/main/images/代码2.jpg?raw=true)