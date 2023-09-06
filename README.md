# Impacket_For_Web


本项目对Impacket进行定制与拓展，增加代理隧道、增加Web API、增加可视化前端。


# 特性
+ Socks 隧道：强大的代理功能，确保稳定的网络通信，独立于任何特定的网络环境。
+ 公网部署 & 多用户支持：本项目支持在公网上部署，多个用户可以同时操作和协作。
+ WebAPI 接口：为前端设计提供了强大的数据交互功能，同时支持简易的集成和二次开发。
+ 免除复杂参数：无需复杂的命令行参数，可通过友好的界面进行操作，直观展示横向移动的过程和结果


# 功能
+ psexec 密码 OR 哈希命令执行
+ atexec 密码 OR 哈希命令执行
+ wmiexec 密码 OR 哈希命令执行
+ dcomexec 密码 OR 哈希单命令执行
+ 需要新功能可提需求

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

# Dockerfile部署

```
# 拉取项目
git clone https://github.com/XiaoBai-12138/Impacket_For_Web.git
# 进入项目
cd Impacket_For_Web
# 构建镜像
docker build -t impacket_for_web .
# 运行容器
docker run -itd -p 8000:8000 --name Impacket_For_Web impacket_for_web
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