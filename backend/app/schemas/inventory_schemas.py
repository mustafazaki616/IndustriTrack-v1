from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_id: int
    quantity: int
    warehouse_location: str

class InventoryUpdate(BaseModel):
    quantity: int
