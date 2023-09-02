# 在 services/proxy_service.py 文件中
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.proxy import Proxy



def get_proxy(db: Session):
    return db.query(Proxy).filter(Proxy.id == 1).first()


def update_proxy(db: Session, proxy_type: str, proxy_host: str, proxy_port: int, is_active: int):
    db_item: Proxy = db.query(Proxy).filter(Proxy.id == 1).first()
    if db_item is None:
        return {"code": -1, "detail": "代理不存在"}
    db_item.proxy_type = proxy_type
    db_item.proxy_host = proxy_host
    db_item.proxy_port = proxy_port
    db_item.is_active = is_active
    db.commit()
    db.refresh(db_item)
    return {"code": 0, "data": db_item}
