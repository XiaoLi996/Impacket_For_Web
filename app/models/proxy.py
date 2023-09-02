# 在models/proxy.py中
from sqlalchemy import Column, Integer, String, event
from .base import Base  # 从基础模型中导入 Base


class Proxy(Base):
    __tablename__ = "proxy"

    id = Column(Integer, primary_key=True, index=True)
    proxy_type = Column(String, unique=True)
    proxy_host = Column(String, unique=True)
    proxy_port = Column(Integer, unique=True)
    is_active = Column(Integer, default=1)


def insert_initial_data(target, connection, **kwargs):
    result = connection.execute(target.select()).fetchone()
    if not result:  # 检查表是否为空
        connection.execute(target.insert(), {
            "proxy_type": "Socks5",
            "proxy_host": "8.8.8.8",
            "proxy_port": "1080",
            "is_active": 1
        })


event.listen(Proxy.__table__, 'after_create', insert_initial_data)
