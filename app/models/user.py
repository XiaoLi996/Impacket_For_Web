from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from .base import Base  # 从基础模型中导入 Base


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)
        return self.hashed_password

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def change_password(self, new_password: str):
        self.hashed_password = self.set_password(new_password)
        return self.hashed_password
