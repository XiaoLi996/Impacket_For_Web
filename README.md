# Impacket_For_Web

实现让Impacket的几个横向模块可视化

# 特性

+ 可部署公网，多人操作
+ 免除死记各种参数
+ 脚本内Socks隧道、不受工具、环境等限制

# 用法

暂时只支持Linux的Python3.10，其他平台如想使用可借助Docker，后期补充Docker教程

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

哈希传递：

![哈希传递](https://github.com/XiaoBai-12138/Impacket_For_Web/blob/main/images/哈希传递.jpg?raw=true)

设置代理：

![设置代理](https://github.com/XiaoBai-12138/Impacket_For_Web/blob/main/images/设置代理.jpg?raw=true)
