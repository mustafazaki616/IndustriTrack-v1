from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.product_schemas import ProductCreate, ProductResponse
from app.services.inventory_service import inventory_service

router = APIRouter()

# Schema for Stock Adjustment Request within this file for now or move to schemas
class StockAdjustmentRequest(BaseModel):
    product_id: UUID
    warehouse_id: UUID
    quantity_change: int
    reason: str

@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await inventory_service.create_product(db, product_in, current_user.id)

@router.get("/products", response_model=List[ProductResponse])
async def get_products(
    skip: int = 0, 
    limit: int = 100, 
    industry: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await inventory_service.get_products(db, skip, limit, industry)

@router.get("/products/{product_id}")
async def get_product_detail(
    product_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = await inventory_service.get_product_detail(db, product_id)
    # Construct response manually or verify schema match
    # Returning dict matches the dynamic shape requirements
    return {
        **data["product"].__dict__,
        "total_stock": data["total_stock"],
        "stocks": data["stocks"]
    }

@router.post("/adjust-stock")
async def adjust_stock(
    adjustment: StockAdjustmentRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await inventory_service.adjust_stock(
        db, 
        adjustment.product_id, 
        adjustment.warehouse_id, 
        adjustment.quantity_change, 
        adjustment.reason,
        current_user.id
    )

@router.get("/stock-status")
async def get_stock_status(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await inventory_service.get_stock_status(db)
