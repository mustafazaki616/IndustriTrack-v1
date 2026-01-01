# Database Design & Migration Rules

## Schema Standards
- **Primary Keys**: Use UUIDs for primary keys to ensure global uniqueness and security.
- **Auditing**: Every table must generally include:
    - `created_at` (DateTime, UTC)
    - `updated_at` (DateTime, UTC)
    - `deleted_at` (DateTime, nullable, for Soft Deletes)
- **Naming**: Snake_case for table names and column names.

## Relationships & Integrity
- **Foreign Keys**: Always define explicit Foreign Key constraints.
- **Indexes**: Add indices on columns frequently used in `FILTER`, `JOIN`, or `ORDER BY` clauses.

## Migrations (Alembic)
- Never modify the database manually. Always generate a migration script.
- Review auto-generated migration scripts before applying.
- Messages must be descriptive (e.g., `add_user_table` not `migration`).

### Example SQLAlchemy Model

```python
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False, index=True)
    status = Column(String, default="pending", index=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
```
