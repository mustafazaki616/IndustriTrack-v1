from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security
from app.core.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Mock login logic
    return {"access_token": "mock-token", "token_type": "bearer"}

@router.post("/register")
async def register():
    return {"message": "User registered"}
