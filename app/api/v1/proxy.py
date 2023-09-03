# 在 api/v1/proxy.py 文件中
from typing import Any, Union

from fastapi import APIRouter, Depends, Form
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.database import _DATABASE_  # 从这里导入
from app.services.proxy_service import get_proxy, update_proxy

router = APIRouter()


class ProxyData(BaseModel):
    proxy_type: str
    proxy_host: str
    proxy_port: str
    is_active: int


class SuccessResponse(BaseModel):
    code: int
    data: Any


class ErrorResponse(BaseModel):
    code: int
    detail: str


class Item(BaseModel):
    proxy_type: str
    proxy_host: str
    proxy_port: str
    is_active: int

APIResponse = Union[SuccessResponse, ErrorResponse]


@router.get("/get_proxy", response_model=APIResponse)
def Routing_Get_Proxy(db: Session = Depends(_DATABASE_)):
    db_item = get_proxy(db)
    if db_item is None:
        return ErrorResponse(code=-1, detail="代理不存在")

    data = ProxyData(
        proxy_type=db_item.proxy_type,
        proxy_host=db_item.proxy_host,
        proxy_port=db_item.proxy_port,
        is_active=db_item.is_active
    )
    return SuccessResponse(code=0, data=data)


@router.post("/set_proxy", response_model=APIResponse)
def Routing_Set_Proxy(item: Item, db: Session = Depends(_DATABASE_)):
    db_item = update_proxy(db, item.proxy_type, item.proxy_host, item.proxy_port, item.is_active)
    if db_item["code"] == -1:
        return ErrorResponse(code=-1, detail="代理不存在")
    return SuccessResponse(code=0, data="修改成功")

