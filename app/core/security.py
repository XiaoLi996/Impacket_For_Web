# 在 core/security.py 文件中
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import _DATABASE_

security = HTTPBasic()


def get_user(db: Session, username):
    return db.query(User).filter(User.username == username).first()


def authenticate(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(_DATABASE_)):
    user = get_user(db, credentials.username)
    if not user or not user.check_password(credentials.password):
        return {"code": 401, "detail": "Incorrect username or password"}
    return credentials.username
