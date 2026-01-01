from sqlalchemy import Column, String, Float, JSON
from app.models.base import BaseERPModel

class Product(BaseERPModel):
    __tablename__ = "products"
    sku = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    bom = Column(JSON)  # Simple BOM storage
