from pydantic import BaseModel, EmailStr
from typing import Optional
from app.core.constants import UserRole

class UserBase(BaseModel):
    email: EmailStr
    role: Optional[UserRole] = UserRole.VIEWER

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: int
    class Config:
        from_attributes = True
 Jonah
class Token(BaseModel):
    access_token: str
    token_type: str
