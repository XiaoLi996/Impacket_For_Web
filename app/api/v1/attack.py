# 在 api/v1/attack_service.py 文件中
from fastapi import APIRouter, Depends, HTTPException, status, Form, Response
from pydantic import BaseModel
from app.services.attack_service import any_exec
from sqlalchemy.orm import Session
from app.core.database import _DATABASE_

router = APIRouter()


class Item(BaseModel):
    hostname: str
    username: str
    password: str
    command: str
    is_hash: int
    exec_method: str


@router.post("/attack")
def create_user_endpoint(item: Item, db: Session = Depends(_DATABASE_)):
    print(item.is_hash)
    res = any_exec(db, item.hostname, item.username, item.password, item.command, item.exec_method, item.is_hash)
    return res
