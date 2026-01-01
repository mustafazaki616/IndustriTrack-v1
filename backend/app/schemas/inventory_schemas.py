from pydantic import BaseModel
from typing import Optional
from backend.app.schemas.product_schemas import ProductResponse

class StockBase(BaseModel):
    quantity: int
    reserved_quantity: int = 0

class StockResponse(StockBase):
    warehouse_id: str  # UUID as str
    last_movement: Optional[str]
    
    class Config:
        from_attributes = True

class ProductStockResponse(ProductResponse):
    total_stock: int
    warehouses: list[StockResponse]
