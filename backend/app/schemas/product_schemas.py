from pydantic import BaseModel
from typing import Optional, List, Dict

class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: float
    bom: Optional[Dict] = None

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: int
    class Config:
        from_attributes = True
