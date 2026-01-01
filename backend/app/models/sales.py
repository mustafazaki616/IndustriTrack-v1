from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.models.base import BaseERPModel

class Customer(BaseERPModel):
    __tablename__ = "customers"
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String)

class SalesOrder(BaseERPModel):
    __tablename__ = "sales_orders"
    customer_id = Column(Integer, ForeignKey("customers.id"))
    total_amount = Column(Float)
    status = Column(String)
