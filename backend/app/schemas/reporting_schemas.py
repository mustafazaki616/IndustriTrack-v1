from pydantic import BaseModel
from typing import Dict, List

class KPIReport(BaseModel):
    name: str
    value: float
    unit: str
    trend: str
