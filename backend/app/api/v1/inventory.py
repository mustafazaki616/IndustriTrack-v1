from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_inventory():
    return {"items": []}

@router.post("/adjust")
async def adjust_stock():
    return {"message": "Stock adjusted"}
