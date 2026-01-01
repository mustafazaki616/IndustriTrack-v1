from sqlalchemy import Column, String, Enum
from app.models.base import BaseERPModel
from app.core.constants import UserRole

class User(BaseERPModel):
    __tablename__ = "users"
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default=UserRole.VIEWER)
