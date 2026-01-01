# FastAPI Backend Development Rules

## Technology Stack
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0 (Async)
- **Validation**: Pydantic V2
- **Auth**: JWT (OAuth2)

## Code Style & Standards
- **Type Hints**: Mandatory for all function arguments and return types.
- **Async/Await**: Use `async` def for all route handlers and database operations.
- **Docstrings**: Required for all complex functions and API endpoints.

## Project Structure
- `app/models/`: SQLAlchemy database models.
- `app/schemas/`: Pydantic schemas (Request/Response models).
- `app/api/`: API route handlers (Controllers).
- `app/services/`: Business logic layer. **Business logic must not reside in route handlers.**
- `app/core/`: Configuration, security, and utility functions.

## Model Guidelines
- All models must inherit from `Base` (SQLAlchemy declarative base).
- **Timestamps**: All models must include `created_at` and `updated_at` columns.

## API Patterns
- Use appropriate HTTP methods (GET, POST, PUT, DELETE, PATCH).
- Return appropriate HTTP status codes (200, 201, 204, 400, 401, 403, 404).
- Use `HTTPException` for error handling.

### Example Endpoint

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    """
    Create a new user.
    """
    user = await user_service.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    user = await user_service.create(db, obj_in=user_in)
    return user
```
