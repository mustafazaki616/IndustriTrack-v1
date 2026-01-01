from sqlalchemy import Column, Integer, ForeignKey, String, Enum
from app.models.base import BaseERPModel
from app.core.constants import WorkOrderStatus

class WorkOrder(BaseERPModel):
    __tablename__ = "work_orders"
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    status = Column(String, default=WorkOrderStatus.PLANNED)
