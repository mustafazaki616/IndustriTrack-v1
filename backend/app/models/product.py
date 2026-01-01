from sqlalchemy import String, Text, Boolean, Integer, ForeignKey, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from datetime import datetime
import uuid

from app.database.base import BaseModel


class Product(BaseModel):
    """SKU Master - Products available in the system"""
    __tablename__ = "products"

    sku: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    industry: Mapped[str] = mapped_column(String(50), nullable=False)  # textile, pharma, food, metal, packaging
    unit_cost: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    selling_price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    reorder_point: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    safety_stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    max_stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_by: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    # Relationships
    stocks: Mapped[List["Stock"]] = relationship("Stock", back_populates="product")
    bom_as_finished: Mapped[List["BOM"]] = relationship("BOM", foreign_keys="BOM.finished_product_id", back_populates="finished_product")
    bom_as_component: Mapped[List["BOM"]] = relationship("BOM", foreign_keys="BOM.component_id", back_populates="component")

    __table_args__ = (
        Index('ix_products_industry', 'industry'),
        Index('ix_products_is_active', 'is_active'),
    )

    def __repr__(self):
        return f"<Product {self.sku}: {self.name}>"


class Warehouse(BaseModel):
    """Warehouse / Storage Location"""
    __tablename__ = "warehouses"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    stocks: Mapped[List["Stock"]] = relationship("Stock", back_populates="warehouse")

    def __repr__(self):
        return f"<Warehouse {self.name}>"


class Stock(BaseModel):
    """Stock levels per product per warehouse"""
    __tablename__ = "stocks"

    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False, index=True)
    warehouse_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("warehouses.id"), nullable=False, index=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    reserved_quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)  # For pending orders
    last_movement: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_by: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    # Relationships
    product: Mapped["Product"] = relationship("Product", back_populates="stocks")
    warehouse: Mapped["Warehouse"] = relationship("Warehouse", back_populates="stocks")

    __table_args__ = (
        Index('ix_stocks_product_warehouse', 'product_id', 'warehouse_id', unique=True),
    )

    def __repr__(self):
        return f"<Stock {self.product_id} @ {self.warehouse_id}: {self.quantity}>"


class BOM(BaseModel):
    """Bill of Materials - Component relationships"""
    __tablename__ = "bom"

    finished_product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False, index=True)
    component_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False, index=True)
    quantity_needed: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    unit: Mapped[str] = mapped_column(String(50), nullable=False)  # kg, pieces, meters, liters
    sequence: Mapped[int] = mapped_column(Integer, nullable=False, default=0)  # Order of components

    # Relationships
    finished_product: Mapped["Product"] = relationship("Product", foreign_keys=[finished_product_id], back_populates="bom_as_finished")
    component: Mapped["Product"] = relationship("Product", foreign_keys=[component_id], back_populates="bom_as_component")

    __table_args__ = (
        Index('ix_bom_finished_component', 'finished_product_id', 'component_id', unique=True),
    )

    def __repr__(self):
        return f"<BOM {self.finished_product_id} <- {self.component_id}>"


class Customer(BaseModel):
    """Customer master data"""
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    credit_limit: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    industry: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    created_by: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    __table_args__ = (
        Index('ix_customers_industry', 'industry'),
    )

    def __repr__(self):
        return f"<Customer {self.name}>"
