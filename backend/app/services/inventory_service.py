from typing import List, Optional
from uuid import UUID
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.product import Product, Stock, Warehouse
from app.schemas.product_schemas import ProductCreate
from app.schemas.inventory_schemas import StockResponse
from datetime import datetime

class InventoryService:
    async def create_product(self, db: AsyncSession, product_in: ProductCreate, user_id: UUID) -> Product:
        # Check if SKU exists
        result = await db.execute(select(Product).where(Product.sku == product_in.sku))
        if result.scalars().first():
            raise HTTPException(status_code=400, detail="SKU already exists")
        
        # Create Product
        product = Product(
            **product_in.model_dump(),
            created_by=user_id
        )
        db.add(product)
        await db.commit()
        await db.refresh(product)
        return product

    async def get_products(self, db: AsyncSession, skip: int = 0, limit: int = 100, industry: Optional[str] = None) -> List[Product]:
        query = select(Product).offset(skip).limit(limit).order_by(Product.sku.asc())
        if industry:
            query = query.where(Product.industry == industry)
        
        result = await db.execute(query)
        return result.scalars().all()

    async def get_product_detail(self, db: AsyncSession, product_id: UUID):
        # Allow string to uuid conversion if needed, though FastAPI handles it
        result = await db.execute(select(Product).where(Product.id == product_id))
        product = result.scalars().first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Get stocks
        stocks_result = await db.execute(select(Stock).where(Stock.product_id == product_id))
        stocks = stocks_result.scalars().all()
        
        total_stock = sum(s.quantity for s in stocks)
        
        return {
            "product": product,
            "total_stock": total_stock,
            "stocks": stocks
        }

    async def adjust_stock(self, db: AsyncSession, product_id: UUID, warehouse_id: UUID, quantity_change: int, reason: str, user_id: UUID):
        # Get Stock record
        result = await db.execute(select(Stock).where(
            Stock.product_id == product_id,
            Stock.warehouse_id == warehouse_id
        ))
        stock = result.scalars().first()
        
        quantity_before = 0
        
        if stock:
            quantity_before = stock.quantity
            stock.quantity += quantity_change
            stock.last_movement = datetime.utcnow()
            stock.updated_by = user_id
        else:
            # Create new stock record if positive change
            if quantity_change < 0:
                 raise HTTPException(status_code=400, detail="Cannot reduce stock for non-existent record")
            
            stock = Stock(
                product_id=product_id,
                warehouse_id=warehouse_id,
                quantity=quantity_change,
                last_movement=datetime.utcnow(),
                updated_by=user_id
            )
            db.add(stock)
        
        if stock.quantity < 0:
             raise HTTPException(status_code=400, detail="Insufficient stock")

        await db.commit()
        await db.refresh(stock)
        
        return {
            "product_id": product_id,
            "warehouse_id": warehouse_id,
            "quantity_before": quantity_before,
            "quantity_after": stock.quantity,
            "reason": reason
        }

    async def get_stock_status(self, db: AsyncSession):
        # Find low stock items
        query = select(Product).where(Product.is_active == True)
        result = await db.execute(query)
        products = result.scalars().all()
        
        low_stock_items = []
        total_value = 0
        
        for p in products:
            # Get total stock
            s_res = await db.execute(select(func.sum(Stock.quantity)).where(Stock.product_id == p.id))
            total_qty = s_res.scalar() or 0
            
            total_value += float(p.unit_cost) * total_qty
            
            if total_qty < p.reorder_point:
                low_stock_items.append({
                    "id": p.id,
                    "sku": p.sku,
                    "name": p.name,
                    "current_stock": total_qty,
                    "reorder_point": p.reorder_point
                })
                
        return {
            "low_stock_items": low_stock_items,
            "total_inventory_value": total_value
        }

inventory_service = InventoryService()
