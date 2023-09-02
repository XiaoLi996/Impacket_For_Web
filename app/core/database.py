# 在core/database.py文件中
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from fastapi import Depends


from app.models import proxy

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据库表
Base.metadata.create_all(bind=engine)


# 这是获取数据库会话的依赖项
def _DATABASE_():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
