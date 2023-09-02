# 在models/ip.py中
from sqlalchemy import Column, Integer, String
from .base import Base  # 从基础模型中导入 Base


class IPAddress(Base):
    __tablename__ = "ip_address"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, unique=True)