from pydantic import BaseModel
from app.core.constants import WorkOrderStatus

class WorkOrderBase(BaseModel):
    product_id: int
    quantity: int
    status: WorkOrderStatus = WorkOrderStatus.PLANNED

class WorkOrderCreate(WorkOrderBase):
    pass
