from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    industry: str
    unit_cost: float
    selling_price: float
    reorder_point: int
    safety_stock: int
    max_stock: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
