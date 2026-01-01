from sqlalchemy import Column, Integer, ForeignKey, String
from app.models.base import BaseERPModel

class StockItem(BaseERPModel):
    __tablename__ = "inventory"
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=0)
    warehouse_location = Column(String)
