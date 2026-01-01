from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class SalesOrderBase(BaseModel):
    customer_id: int
    total_amount: float
    status: str
